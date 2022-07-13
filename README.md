# ROOMBOT 2.0


     ________  ________  ________  _____ ______   ________  ________  _________   
    |\   __  \|\   __  \|\   __  \|\   _ \  _   \|\   __  \|\   __  \|\___   ___\ 
    \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \  \ \  \|\ /\ \  \|\  \|___ \  \_| 
     \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \\\  \   \ \  \  
      \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \\\  \   \ \  \ 
       \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\ \_______\ \_______\   \ \__\
        \|__|\|__|\|_______|\|_______|\|__|     \|__|\|_______|\|_______|    \|__|
                                                                              
                                                                              
                                                                              
     
       


En løsning på å automatisk booke grupperom på HVL!
   
                      Versjon: 
                      2.0
 


Det har vist seg at mange studenter på HVL løser grupperombookingen på HVL ved å ha alarm på klokka 22:00, da websiden åpner for booking 3 dager frem i tid.\ Dette for å raskest mulig å kunne booke seg et rom så man har et sted å arbeide med venner.



Som Dataingeniørstudent var det helt uaktuelt å synke så lavt å gjøre manuelt arbeid. Så da er løsningen et script som booker et rom jeg vil ha med\ maskinpresisjon før alle andre.

Dette har vært et krevende prosjekt som har tvunget meg å lære flere backendaspekter, og jeg er overlykkelig at det funker!\
Applikasjonen ligger på www.birkjohannessen.com \

Teknologier/språk som er brukt: php, html, python, nginx, mysql, linux.
\
prosjektet startet med å leie domenet birkjohannessen.com og linke det til linuxserveren min.\
Deretter var det å konfiguere nginx til å hoste all trafikk på port 443, dette er på en offentlig nøkkel som ikke er CA godkjent.\
Så er det en login side som kobler opp til en mysql database lokalt på serveren. passordene er hashet og saltet og cookien er kryptert.\
Når man logger inn har man mulighet å velge forskjellige parametere for å så kunne booke. disse dataene blir koblet opp og lagret i mysql databasen\
Deretter kan en se på brukerens aktive bookinger og mulighet å fjerne de (fra databasen).\
Det sensitivet passordet brukeren oppgir her blir kryptert i databasen til den hensikt at jeg ikke skal se passordet i klartekst under vedlikehold/debugging.\
På serveren er det en crontab som kjører et pythonscript klokken 22:00 hver dag,\
dette scriptet tar alle entries fra databasen og kjører det opp mot timeedit.\
itillegg er det en admin side, som har tilgang å se oversikt og slette på brukere og aktive bookinger i databasen.\






Laget av Birk Johannessen.
