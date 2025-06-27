#!/bin/bash

git config --global user.name "Renara Soares"
git config --global user.email "r.soares@aluno.ifce.edu.br"

cp ~/.ssh/20231321000034 ~/.ssh/id_ed25519
cp ~/.ssh/20231321000034.pub ~/.ssh/id_ed25519.pub

chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub

echo "Configuração concluída!"
