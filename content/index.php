<?php
$gszLang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);
switch ($gszLang)
{
    case "fr":
        header('Location: /fr/');
        break;
    default:
        header('Location: /en/');
        break;
}
?>
