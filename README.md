# okd-cicd-workshop
Dit is een voorbeeld dat gebruikt wordt in de workshop experience voor CI/CD die
aan verschillende teams wordt gegeven. 

--------------------------------------------------------------------------------
# Voorbereiding van de workshop
- Maak een nieuwe repo aan met de naam `<kies-team-naam>-cicd-workshop`
- Kopieer de inhoud van deze repo naar de nieuwe repo. Voordat je de eerste commit
  uitvoert, verwijder een aantal comments in de applicatie-code onder folder 
  app. Hierdoor faalt Pylint en opdracht van het team is om dit te fixen.
- Wijzig de `Jenkinsfile`.
- Wijzig de `pipeline-template.yaml`.
- Wijzig de `README.md` zoals de titel!
- In de presentatie verwijzingen naar het team vervangen. Zie /docs
- Zorg dat de nieuwe repo de master branch in de OTAP hangt van het team waaraan
  de workshop wordt gegeven. Github teams, Jenkins user in de repo en evt de webhook.
- Deze tekst verwijderen!
--------------------------------------------------------------------------------

# Oefeningen
Deze repository dient als basis om de ci/cd workshop mee te geven. Volg de 
oefeningen hieronder stap-voor-stap. Veel plezier!

## Oefening 1: Maak een feature branch in Github
Wanneer je nieuwe functionaliteit ontwikkelt, dan doen we dat op een feature 
branch in Github.
- Ga in Github naar de repository die je als team hebt gekregen. En klik op de
  popup met de verschillende branches. Maak een nieuwe branch met de naam:
  feature-<kies een eigen naam>
- Ga naar de feature branch in Github en wijzig de Jenkinsfile. Voeg de feature
  branch toe aan de 'buildStrategy'. Pas de stappen aan die in de feature branch
  worden uitgevoerd. Bijvoorbeeld alleen bouwen en deployen naar dev, bijvoorbeeld:
  ```
    'feature-new-branch': [ 'checkout', 'build', 'containerize', deploy:dnb-got-dev'
    ]
  ```
  **Letop**: Zet in plaats voor het sterretje de naam master neer (in de huidige Jenkinsfile.Openshift)!
  
  #### Een andere letop is dat elke feature branch zijn eigen route, service en deploymentconfig heeft! (zie folder oc). Pas ook deze aan voor de specifieke feature branch (anders gebruikt jouw buurman dezelfde service en route)!
  
  **Tip**: Je kunt de file direct wijzigen in Github en een commit uitvoeren. Wanneer
  je meer wilt oefenen met het doen van wijzigingen, wijzig dan bijvoorbeeld
  de README.md file. Je kunt ook Github Desktop gebruiken. Op het intranet staat
  hoe je deze kunt installeren (proxy).

## Oefening 2: Een build pipeline aanmaken in Openshift
- Login in Openshift en bekijk de eigen namespaces waar je toegang toe hebt.
- Ga naar de namespace van de specifieke OTAP omgeving: newbusiness-forza-ops
- Importeer een yaml (rechts bovenin in het menu) en kopieer/plak de inhoud van file `pipeline-template.yaml`. Let op
  dat je de velden branch en repo naam goed invult.
- Start de build pipeline.
- Controleer de uitkomst in Jenkins. De build faalt (en dat is
  de bedoeling). In de volgende oefening ga je de build repareren.



## Oefening 3: Corrigeren van fouten (deprecated)
- Het blijkt dat de pipeline faalt. Code quality (Pylint) geeft een fout. 
  Corrigeer deze in de repository op Github en start opnieuw de build pipeline.
- Check of de API beschikbaar is in de dev omgeving. De volgende url is beschikbaar
  voor de API: `https://<name_repo>-<namespace>.apps.okd.alliander.com/api/v1/docs`
  Hier staat wat documentatie. De <name_repo> is bijvoorbeeld got-cicd-workshop en
  <namespace> is bijvoorbeeld dnb-got-dev.
- Extra/optioneel: Je kunt elk gewenste naam claimen die voor 
  `apps.okd.alliander.com` staat. Weet je hoe? Vraag de cursusleider of probeer
  de route direct via de console te wijzigen.

## Oefening 4: Sonar quality gates (deprecated)
In Sonar wordt de kwaliteit van de code weergegeven. Je kunt onder andere zien
dat er code-smells in de code zitten en dat een unit test leeg is opgeleverd.
Je kunt Sonarqube oproepen door onder routes te kijken naar SonarQube. Wanneer
Sonarqube met een inlogscherm komt, dan is het standaard username/wachtwoord admin.
Sonarqube zit achter de netscaler en kan niet benaderd worden door mensen buiten
Alliander.
- Implementeer een geldige unit test (folder tests). Start opnieuw de build pipeline
  en controleer of in Sonarqube de code-smell is opgelost?
- Klik eens door SonarQube...

## Oefening 5: API aanpassen (deprecated)
API's zijn een manier om functionaliteit in de applicatie te ontkoppelen en aan
te bieden aan derden. In de nabije toekomst worden de API's aangeboden in het API
management platform waarbij de API's tentoongesteld worden in een etalage.
Het voorbeeld is geschreven in Python en maakt gebruik van de FastAPI package. Dit is een
asynchroon webframework waarmee je snel en effectief API's kunt ontwikkelen. Deze
API is een blackjack voorbeeld. Probeer zelf eens een API call toe te voegen aan de
hand van hetgeen er reeds is.
- Maak een API GET-method die de string "Hello World!" terug geeft. Zorg er voor
  dat Pylint goed is en dat er een unit test is toegevoegd.
- Probeer ook eens de documentatie van de API aan te passen!

## Oefening 6: Pull request naar Master (deprecated)
Wanneer een ontwikkelaar klaar is met het ontwikkelen van nieuwe functionaliteit,
dan worden de wijzigingen terug gevoerd naar de Master branch. Dit is de branch
waar alle wijzigingen van andere ontwikkelaars bij elkaar komen (mergen). Dit
doen we door een Pull request aan te maken.
- Maak in Github een Pull request en ken deze toe aan een van de teamleden. Dit 
  teamlid kan een code-review uitvoeren en uiteindelijk aangeven dat de code
  goed is om naar de main branch (master) te mergen.
- Laat een teamlid de pull request accepteren en de wijzigingen mergen naar
  master. Let er op dat je waarschijnlijk niet alle files wilt mergen naar de
  master zoals de pipeline definitie of de Openshift configuratie files.
- Laat de master opnieuw bouwen in Openshift.

## Oefening 7: Beheer is cool, Ops is cooler (deprecated)
Inmiddels weet je dat er verschillende containers draaien. Vanuit de Openshift
console kun je direct toegang krijgen tot de container middels een Linux 
terminal.
- Voer eens het commando `top`, `ps -aux` of `ls -l` uit.
- Met het commando `curl -v` kun je ook de API bereiken op localhost en in de
  container testen of de API werkt. Probeer eens de API call aan te roepen die
  je zelf zojuist hebt geimplementeerd?

# Extra informatie: Wanneer je lokaal wilt ontwikkelen?
Hieronder staan specifieke Python commando's om dit voorbeeld lokaal op een laptop
uit te proberen en aan te passen.

### Aanmaken Python virtual omgeving
```
$ virtualenv -p `which python3` venv --always-copy
$ source venv/bin/activate
$ pip install -r requirements.txt
````

### Packages installeren
```
$ pip install <name-of-package>
$ pip freeze > requirements.txt
```

### Starten webserver op poort 8080
```
$ uvicorn app.main:app --reload --port 8080
```

### Checken codestyle
```
$ pylint app
```

### Uitvoeren unit tests
```
$ pytest
```
## Doel van deze repository
Deze repository wordt in workshops gebruikt, echter ook tijdens het ontwikkelen 
van de CI/CD omgeving. De bedoeling is dat deze repository een basis is voor iedereen
die hier mee aan de slag wil gaan en dat het een basis is om nieuwe functionaliteit
toe te voegen aan CI/CD. Op deze manier heeft deze twee doelen!

Deze repository werkt in de basis voor alle stappen in de buildstraat. Middels
oefeningen wordt functionaliteit toegevoegd en gaan er zaken anders dan je zou
verwachten. De oefeningen zoals hierboven beschreven leiden je stap-voor-stap
door dit proces.

Er is een repository met de naam postcode-location. Dit is dezelfde functionaliteit, 
echter is deze repository gebasseerd op modernere Python libraries en bevat meer
functionaliteit zoals PyLint, Unit tests met PyTest, Robot tests etc...