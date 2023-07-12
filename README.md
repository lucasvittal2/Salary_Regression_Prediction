# Salary_Regression_Prediction 📈 

Como proposta do MVP parte 1 parte II da minha pós-graduação em ciência de dados e analytics, propus a mim mesmo o seguinte problema:

Vamos supor que o gestor de uma empresa 👨‍💼 deseja ter mais controle do budget 💸💰 para investir em projetos. Em muito casos existem projetos que solicitam contratação de mais mão de obra. Porém o gestor deve estar atento a não ultrapassar o valor que ele tem dispível para efetuar a contratação do profissional que precisa,  conseguir estimar por sí só seria uma tarefa extramamente difícil e emprecisa, o que pode fazer com que facilmente se estoure o orçamento. A empresa possui uma base de dados de todos os contratado até aquele momento, sendo assim, para que se haja maior controle no orçamento, o gestor gostaria de um modelo de machine learning que seja capaz de prever quanto seria o salário de um novo contratado, assim o gestor consegue traçar com mais precisão o perfil de profissional que ele pode contratar  de modo que não estoure o orçamento.


Tendo em vista o  esquema do banco de dados diponibilizado pela empresa:

```
   age -> Idade do empregado
   experience -> Nível de experência profissional
   job role -> Cargo Ocupado
   education level -> Grau de Educação
   salary -> Salário anual em USD$
```
Primeiramente vamos analisar os dados que temos para identificar todos os pré-processamento necessário e possíveis variáveis a serem eliminadas, posteriormente vamos selecionar os modelos que se enquandram nesse tipo de problema, pefromar o cross-validation, optimizar os hiperparâmetros e em seguida fazer novamente o cross validation novamente. Logo após esssa etapa teremos o modelo com melhor performance e  assim faremos nele uma avalição através do Holdout(treino/test). Por fim treinameremos o melhor modelo selecionado como todos os dado disponbilizados para que assim se possa colocar os modelo treinado em produção para ser utilizado pelo gestor da empresa na hora de estimar os perfis que cabem no seu orçamento.

O o notebook assim como suas dependencias podem ser encontrados em:



dentro da pastas Code.

Já a pasta do projeto com todos os arquivos e dependências pode ser acessada abaixo:

[Regression Salary Prediction Project Folder](https://drive.google.com/drive/folders/1mKxH7_GjddefY2MBM7_j6hkiaTuf9N3u?usp=sharing)

O notebook encontra-se dentro da pasta Code.

