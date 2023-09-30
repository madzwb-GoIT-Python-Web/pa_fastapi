switch -File .env {
    default {
        $name, $value = $_.Trim() -split '=', 2
        if ($name -and $name[0] -ne '#') { # ignore blank and comment lines.       
            $name.Trim()
            $value.Trim()
            Set-Item "Env:$name" $value   
        }
   }
}
