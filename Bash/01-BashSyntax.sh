#!/usr/bin/env sh
# I - prompt user

echo "Hello $USER"

# II - receive arguments

name="Adrien"

echo "Hello $name"

# III - path to

path="/home/adrien/Github"

if [ -z "$path" ]; then
    echo "Erreur : Veuillez fournir un chemin en argument."
    exit 1
fi

if [ ! -e "$path" ]; then
    echo "Erreur : Le chemin '$path' n'existe pas."
    exit 1
fi

if [ -f "$path" ]; then
    if [ "$(file --mime-type -b "$path" | cut -d'/' -f1)" = "text" ]; then
        cat "$path"
    else
        echo "Erreur : '$path' n'est pas un fichier texte."
        exit 1
    fi
fi

if [ -d "$path" ]; then
    echo "Contenu du répertoire '$path' :"
    find "$path" -maxdepth 1 -type f \( -iname "*.txt" \) -exec cat {} +
fi

# IV - information

echo "user: $USER Date: $(date) Directory: $PWD"

# V - list of groups

echo "Entrez le nom d'utilisateur : \c"
read -r username

echo "L'utilisateur '$username' fait partie des groupes suivants :"
groups "$username" | tr ' ' '\n' | sed "s/^/$username fait partie du groupe /"
