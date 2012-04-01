Materiale til workshop om enkel ytelsestesting med [Grinder](http://grinder.sourceforge.net), med fokus på testing av websider/applikasjoner.

[Slides here](http://kvalle.github.com/grinder-workshop/).

TODO: mer info om workshoppen.

# Forberedelser

For å spare tid vil det være fint om alle kan gjøre noen forberedelser før workshoppen begynner.
Vi kan da begynne rett på arbeidet med oppgavene, uten å måtte installere og sette opp Grinder først.

Det du trenger å gjøre er:

- Hvis nødvendig, installer [git](http://git-scm.com/download).
- Hvis nødvendig, installer [Java](http://java.com/en/download).
- Sjekk ut dette repositoriet.

    git clone git://github.com/kvalle/grinder-workshop.git

Når du er ferdig med å installere kan du sjekke at alt fungerer ved å kjøre eksempel-testen (når du står i mappen `grinder-workshop`):

    ./startAgent.sh example/example.properties
  
Når du kjører dette eksempelet vil Grinder skrive ut en del informasjon.
Først kommer det litt informasjon om hva som skjer under oppstarten, og muligens noen linjer med noe slikt som `*sys-package-mgr*: processing new jar`.
Ignorer dette for nå.

Deretter skriver selve eksempel-testene ut litt info mens de kjøres.
Dette bør se ut omtrent som følgende:

    > output #0 from worker thread 1
    > output #0 from worker thread 0
    > output #1 from worker thread 0
    > output #1 from worker thread 1
    > output #2 from worker thread 0
    ...

Når testen har kjørt ferdig kan du i tillegg sjekke at alt har gått riktig for seg ved å titte på resultatet som skal ha blitt lagret i den nyopprettede mappen `grinder-workshop/log`.
Her skal det ligge to filer med navn som `out_xyz-0.log` og `data_xyz-0.log`, der `xyz` er navnet på din datamaskin.
I `out`-filen finner du et sammendrag av testens resultater, og `data`-filen inneholder alle detaljene i et komma-separert format.
Hvis alt har gått bra skal det *ikke* være laget noen filer med navn som `error_xyz-0.log`!

*Hvis du av en eller annen grunn ikke kan installere git går det også an å laste ned [koden som zip-fil](https://github.com/kvalle/grinder-workshop/zipball/master).*

# Ressurser

Vi har forsøkt å forklare hva som skal gjøres i oppgavene så godt vi kan, men det dukker naturligvis alltid opp spørsmål.
I tilfelle vi ikke umiddelbart er tilgjengelige for å svare på disse, oppsummerer vi de viktigste stedene å finne informasjon under.

## Grinder

For informasjon om Grinder er [hjemmesiden](http://grinder.sourceforge.net/) et greit sted å starte.
Det nyttigste stedet å starte for å lage test-script er [script-galleriet](http://grinder.sourceforge.net/g3/script-gallery.html) som inneholder en rekke gode eksempler.
Det finnes også et [script API](http://grinder.sourceforge.net/g3/script-javadoc/index.html) med forklaringer på hvordan de forskjellige klassene og metodene fungerer.

## Python

Det første stedet å sjekke om du har spørsmål til selve språket er [Pythons offisielle dokumentasjonen](http://docs.python.org/index.html).
Her ligger veldig mye og god informasjon.
En god måte å finne frem til denne er via [søkesiden](http://docs.python.org/search.html).
For eventuelle spørsmål som går på samspillet mellom Python og Java er [hjemmesiden til Jython](http://www.jython.org/docs/index.html) stedet å starte.

# Oppgaver

Oppgavene er beskrevet under.
Det går fint an å løse oppgavene på egenhånd, men vi anbefaler å sitte to og to sammen.

Vi starter svært enkelt med å måle responstid for GET over HTTP med én enkelt URL.
Oppgavene blir gradvis vanskeligere, og vi vil komme innom blant annet sjekking av responser, generering av script ved hjelp av HTTPProxy, og testing av REST-API.

Siden dette er en workshop om Grinder og ikke Python, gir vi for hver oppgave tips om funksjoner det kan være greit å vite om.
Vi er også tilgjengelige under hele workshoppen, så ikke nøl med å spørre om hjelp.

Løsningsforslag til alle oppgavene ligger under `solutions/`.


## Oppgave 1 - Enkel testing av responstid

I den første oppgaven skal du skrive en Grinder-test som måler responstiden mot en enkelt URL over HTTP.

For å hjelpe deg i gang har vi laget litt kode du kan ta utgangspunkt i.
Vi har laget en ferdig properties-fil `tests/1.properties` som inneholder testkonfigurasjonen.
Denne peker på testscriptet `tests/scripts/test1.py` som du må gjøre ferdig selv.

For å kjøre testen kan du bruke `startAgent` scriptet på følgende måte:

    ./startAgent.sh tests/1
   
Det er tre ting som må gjøres:

1. Opprett et `Test` med nummer og beskrivelse.
2. Wrap en `HTTPRequest` med testen.
3. Gjør en GET hver gang `__call__`-metoden blir kalt.


## Oppgave 2 - Testing av mange URLer om gangen

Akkurat som i oppgave 1 har vi gjort klart properties-fila `tests/2.properties` og et skall for scriptet i `tests/scripts/task2.py`.

Filen `tests/scripts/urls.txt` inneholder en rekke URL-er.
Oppgaven er ikke mye vanskeligere enn den forige, og går rett og slett ut på å lage et script som leser denne filen, og tester samtlige URL-er.
Pass på å få laget en `Test` for hver URL slik at responstidene måles individuelt.

Testscriptet skal altså:

- Lese URL-ene fra filen.
- Lage tester for hver URL.
- GETe hver enkelt URL hver gang scriptet kjøres (altså, hver gang `__call__`-metoden i `TestRunner` blir kalt).

### Ekstraoppgave:

Blir du raskt ferdig må du gjerne prøve deg på følgende:

- Legg beskrivelser av hver test/URL sammen med URL-ene i `urls.txt`, og bruk disse når du oppretter `Test`-ene.
- I stedet for å wrappe `HTTPRequest` med testene slik vi gjorde i oppgave 1, opprett i stedet lambda-funksjoner for å kalle GET med hver enkelt URL.
  Disse kan i stedet wrappes av testene, slik du slipper å holde styr på listen av URL-er i `__call__` metoden.


## Oppgave 3 - Validering av responser

I oppgave 3 er det ikke laget noen kode å ta utgangspunkt i -- i stedet bygger vi videre på løsningen fra oppgave 2.
Dersom du ikke ferdig med forrige oppgave, men likevel har lyst til å begynne med denne, kan du sjekke løsningsforslaget i `solutions/2.properties` og `solutions/scripts/task2.py`.

Oppgaven går ut på å få testene til å se nærmere på responsene vi får tilbake.
Så langt har vi gjort GET requests mot de forskjellige URL-ene, og registrert alle forepørsler som har gitt svar som suksesser.
Du skal nå legge på noen respons-sjekker som feiler tester dersom vi ikke får tilbake det vi forventer.

Du velger selv hva du ønsker å teste.
(Her er det bare fantasien som setter begrensninger!)
Noen forslag til ting som kan testes på en enkel måte er

- at HTTP statuskode er 200
- at responsen har en viss minimum størrelse (i linjer eller byte)
- at responsen (ikke) inneholder en gitt tekst

For å styre hvorvidt Grinder skal gjenkjenne gjennomføringen av en test som velykket eller ikke bruker vi `grinder.statistics`.
Følgede kan være greie å kjenne til:

* `grinder.statistics.delayReports = 1`  
  Skrur av umiddelbar rapportering av resultater.
  Bruk denne i starten av scriptet slik at vi kan melde inn resultatene manuelt.
* `grinder.statistics.forLastTest.success = 0`  
  Merker testen som ble kjørt sist som feilet.
  Settes automatisk til 1 etter hver test.
* `grinder.statistics.report()`  
  Rapporter resultat for sist kjørte test.

### Ekstraoppgave:

Hvis oppgaven blir enkel kan du utvide med å lage respons-sjekker spesielt tilpasset hver enkelt request.
Dette kan for eksempel løses ved å legge mer informasjon sammen med URL-ene i filen som leses, og bruke denne til å avgjøre hva som skal testes for hver URL.


## Task 4 - Testing of a typical JSON-API (REST API)

Up until now, we have tested some pretty static pages. You (might have) parsed the response to do some basic content-check (e.g. to check whether some specific text are present, or if it's not). Now, it's time to do some more fancy parsing.

We'll be testing against an API which returns JSON. This JSON will contain links to further stuff you can test against. These links will change for each request, this means that we'll have to parse the JSON to fetch the links - we can't hard-core all the links in the script beforehand. This task will prepare you for testing real API's out there, either if they have real links or if they just have ID's you have to parse out and include in a predefined URL-template.

The easiest way to start is to do a manual call against the webpage: http://grinder.espenhh.com/json.php

Take a look at the JSON, and figure out what you want to test. It could be smart to run the JSON through a ["beautifier"](http://jsonformatter.curiousconcept.com/) to be better able to see the structure.

### How-to

Then, start writing the test. We'll give you complete freedom here, but to get you started you can do the following:

1. Start by writing a test that fetches http://grinder.espenhh.com/json.php and outputs the result to the console
2. Now, modify the test to parse the JSON.
3. To start simple, print out the fetched-field on the JSON
4. Now loop through all the tweets, and print out the tweets
5. Find the URL for each tweets profile picture, and do a GET against this URL

If you want to continue doing some JSON testing, you can try the real twitter API. And PLEASE: don't load-test this, just run with a single thread and a single run each time! Load-testing other people's servers without permission is BAD BEHAVIOUR ;)

Twitter: http://search.twitter.com/search.json?q=grinder (change "grinder" to whatever you want)


## Task 5 - Using Grinder's TCPProxy to automatically generate tests

Sometimes, you don't want to write all your tests by hand, you just want to simulate a user clicking through some pages in a browser. Grinder has support for this; by using the [Grinder TCPProxy](http://grinder.sourceforge.net/g3/tcpproxy.html) you can record a web-browsing-session and replay it using Grinder afterward. This technique will also generate a script which you can later modify (this is something you almost certainly would want to do!).

### How-to

Do the following tasks to record a simple web page:

1. Start the proxy server by running the script `./startProxy.sh` .. This will start a simple console that lets you input comments, and stop the proxy cleanly
2. Configure your browser to send traffic through the proxy (read more [here](http://grinder.sourceforge.net/g3/tcpproxy.html) )
3. Go to a simple web page (we recommend starting with http://grinder.espenhh.com/simple/ ). If you go to a complex page, the generated script will be crazy long
4. After the page have loaded in the browser, click "stop" in the simple console window
5. Inspect the script generated: it's located at `proxy/proxygeneratedscript.sh`
6. Try running the script: `./startAgent.sh proxy/proxygeneratedscript.sh`
7. Check the log, try modifying the script, experiment. You can start by removing all the sleep statements in the script. Then try it on a more complicated page. Have fun =)
