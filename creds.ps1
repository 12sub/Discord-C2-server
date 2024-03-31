$strings = (netsh wlan show profiles) | Select-String "\:(.+)$";
foreach($string in $strings) {
    $name=$string.Matches.Groups[1].Value.Trim();
    
    $details = netsh wlan show profile name="$name" key=clear | Select-String "Key Content\W+\:(.+)$";

    if($details.Matches -ne $null) {
        $password = $details.Matches[0].Groups[1].Value.Trim();
    } else {
        $password = "";
    }

    [PSCustomObject]@{
        Profile=$name;
        Password=$password;
    }
}