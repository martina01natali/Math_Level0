## Algebra dolce 1, seconda edizione

*Testo di matematica per il biennio dei licei non scientifici*

## Origine

Questo lavoro è tratto da Matematica $C^3$ il testo libero edito da

[matematicamente.it](www.matematicamente.it)

## Collaborazione

Perché questo progetto non muoia c'è bisogno anche del tuo aiuto!

Per vedere come è possibile collaborare visita il 
[wiki](https://bitbucket.org/zambu/mc3_a1_dolce_2ed/wiki).

In particolare le segnalazioni di errori e le proposte di miglioramento
possono essere fatte partendo dalla pagina:
[issues](https://bitbucket.org/zambu/mc3_a1_dolce_2ed/issues)
compilando il form che si apre cliccando sul pulsante in alto a destra:
*+ create issue*.

## Descrizione

Rispetto all'origina è stata riorganizzata la struttura per seguire
le indicazioni ministeriali relative alla materia.

È stata aggiunta la parte relativa agli elementi di informatica introducendo 
un capitolo sul foglio di calcolo e uno sulla geometria della tartaruga 
trattata con il linguaggio di programmazione Python.

Il testo, pur completo, è ancora giovane e in pieno sviluppo.

In particolare c'è da adattare sia le spiegazioni sia gli esercizi alla 
realtà scolastica a cui il libro si rivolge.

Chiunque abbia materiale, idee, tempo da offrire per contribuire 
all'opera, e anche osservazioni e critiche, è pregato di contattare 
il coordinatore del progetto all'indirizzo sotto elencato.

Con la speranza che puesto testo possa contribuire a far amare la matematica.

## Download

Nella sezione Download (icona a nuvoletta, barra a sinistra ultima in basso) 
trovate sia il testo in formato pdf sia tutto il sorgente in formato Latex.

## Link

Il volume 2 è reperibile da:

[Algebra dolce 2](https://bitbucket.org/zambu/mc3_a2_dolce_2ed/)

## Licenza

Tutto il materiale di questo progetto è rilasciato sotto licenza: CC-BY-SA.

## Coordinatore del progetto

Indirizzo per comunicare con il coordinatore del progetto:
daniele.zambelli@gmail.com

## Readme originale di Matematica C3

Di seguito riporto il file redame originale di Matematica C3.

```
%========================================================% 
% README per Algebra 1                                   % 
% (c) 2013-2014 Dimitrios Vrettos - d.vrettos@gmail.com  %
% v1.0.1 2014/04/15                                      %
% Questo file non si può modificare da terzi             %
% =======================================================%

Il presente file offre informazioni utili per 
l'utente finale ed è suddiviso nelle seguenti parti

 1 - Licenza
 2 - Requisiti
 3 - Compilazione
 4 - Domande e contatti


 1. LICENZA
-----------------------
Il libro 'Algebra 1', eccetto dove diversamente specificato, 
è rilasciato nei termini della licenza Creative Commons 
Attribuzione 3.0 Italia (CC BY 3.0) il cui testo integrale 
è disponibile al sito 
http://creativecommons.org/licenses/by/3.0/deed.it

Il testo integrale della licenza dovrebbe esserci
nella stessa directory del file README. In caso 
contrario, si può visionare sull'inidirizzo:
http://creativecommons.org/licenses/by/3.0/legalcode

Il codice sorgente, che serve per un'eventuale 
compilazione di 'Algebra 1' in LaTeX, viene 
rilasciato con licenza:
LaTeX Project Public License, version 1.3c or later

Anche il testo integrale di questa licenza dovrebbe 
essere presente nella stessa directory del file 
README. In caso contrario, visitare l'indirizzo:
http://www.latex-project.org/lppl.txt

Ogni singolo file *tex, *pgf, *htx riporta il nome e
l'indirizzo e-mail delle persone che hanno lavorato
per la stesura del codice.

 2. REQUISITI
-----------------------
Per l'esigenze del libro sono stati creati un
pacchetto (matc3) e una classe (matc3mem). 
Entrambi sono inseriti nella TeXLive e nella MikTeX.
Se i file non sono presenti, si può sorpassare 
l'installazione manuale, aggiornando la propria 
distribuzione.

Il pacchetto matc3 può essere trovato a:
http://www.ctan.org/tex-archive/macros/latex/contrib/matc3

La classe matc3mem si trova a:
http://www.ctan.org/tex-archive/macros/latex/contrib/matc3mem

Nel primo e nel terzo capitolo si fa uso di gieroglifici. 
Il pacchetto e i font richiesti non sono inclusi nelle 
distribuzioni standard. Per questo motivo è richiesta 
un'installazione manuale.

Il pacchetto HieroTeX è disponbile su:
http://mirrors.ctan.org/fonts/hieroglyph/HieroTeX-3.5.tgz

e i font:
http://mirrors.ctan.org/fonts/hieroglyph/HieroType1-3.1.4.tgz

Infine, per la creazione di alcuni grafici, è stato utilizzato il
programma gnuplot, che dovrà essere presente nella macchina nella
quale si desidera compilare i sorgenti.

Riassumendo:
	1 - matc3 e matc3mem, inclusi nelle versioni aggiornate
	    e complete di TeXLive2012 e MikTeX 2.9 (dall'8 aprile 2013
	    e in poi);
	2 - HieroTeX e HieroType;
	3 - Gnuplot.


 3. COMPILAZIONE
-----------------------
Deve essere compilato il file algebra1_5ed_completo.tex in pdfLaTeX. Poichè
vengono caricati dei programmi esterni, la compilazione deve avere abilitata
l'opzione --shell-escape (o --enable-write18). Se, invece, si desidera
compilare dal terminale, si dia (due volte) il comando
	  $ pdflatex --shell-escape algebra1_5ed_completo.tex
In alternativa, si può utilizzare il Makefile:
   	  $ make pdf
che produce il libro completo.
Per maggiori opzioni, digitare
    	  $ make help

  
 4. DOMANDE E CONTATTI
-----------------------
Per domande e suggerimenti strettamente correlati con il lato tecnico del libro
potete contattare:
Dimitrios Vrettos
d.vrettos@gmail.com
```