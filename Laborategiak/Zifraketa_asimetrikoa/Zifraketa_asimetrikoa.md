# Laborategia: Zifraketa asimetrikoa

## Aurretiazko baldintzak

- GNU/Linux makina: eramangarria, makina birtuala edo laborategiko ordenagailua (LDAP kredentzialarekin saioa hasi).
- Kode-editorea. Visual Studio Code-n, ctrl+mayus+v sakatuz, fitxategi hau ondo ikus daiteke (batez ere irudientzat).
- Beharrezko tresnak: OpenSSL (`sudo apt install openssl`), gpg (`sudo apt install gpg`).
- Ikasgaiaren GitHub biltegia: laborategian garatutako programak igo ditzakezu.

## GPG gakoak sortu

[GnuPG (GPG)](https://gnupg.org/) komunikazioak babesteko informazioa zifratu, deszifratu eta sinatzeko aukera ematen digun programa librea da, [OpenPGP](https://www.openpgp.org/) estandarra betez. GPGk aukera asko eskaintzen ditu. Komeni da haiekin ohitzea:

```bash
gpg --help
```

GPGrekin lan egiteko, lehenik eta behin gako-pare bat sortu behar da (publikoa eta pribatua):

```bash
gpg --generate-key
```

Oso garrantzitsua da email-helbide egokia sartzea. Pasahitza aukerakoa da, eta gako pribatuen giltzarrirako sarbidea babesteko balio du. PGPn, giltzarria gakoak gordetzen diren biltegia da. Gako pribatuen giltzarria eta gako publikoen giltzarria daude. Komeni da giltzarria pasahitz batekin babestea.

`gpg --full-generate-key` komandoa erabiliz, erabili nahi duzuen gakoaren luzera eta hura sortzeko erabili nahi duzuen algoritmoa zehaztu daitezke. GnuPGk RSA, DSA eta ElGamal onartzen ditu. Gako-parea sortzeko, entropia erabiltzen da; gakoak duen ausazkotasun edo desorden kantitatea adierazten du. Zenbat eta entropia handiagoa izan, orduan eta ausazkotasun handiagoa eta, beraz, kriptoanalisia egitea zailagoa. Gakoak sortzean, entropia makinaren datuetan oinarrituta lortzen da, hala nola CPUaren egoeran, datan, irekita dauden leihoen kopuruan eta abar. Beraz, gakoa sortzen den bitartean nabigatzea, leihoak irekitzea, teklatuan idaztea eta abar komeni da, ahalik eta entropia handiena sortzeko.

Gakoak sortu ondoren, gakoak baliogabetzeko ziurtagiri bat sortzeko aukera dago. Baliogabetze-ziurtagiriak gakoa jada baliozkoa ez dela adierazteko balio du, galdu egin duzulako, lapurtu dizutelako eta abar. Sortu baliogabetze-ziurtagiria eta gorde ezazu.

Sortutako gakoak ikusteko:

```bash
gpg --list-keys
```

> Zer esan nahi du `[ultimate]` etiketak?

Nire sistemak konfiantza absolutua daukala gako horrekiko nik sortu dudalako lokalki eta dagokion gako pribatua daukadalako.


Garrantzitsua da gako publikoa eskuragarri egotea. [Web-orri pertsonal](https://mikel-egana-aranguren.github.io/contact/) batean argitara daiteke, email batean erantsita bidal daiteke edo zerbitzari espezifikoetan argitara daiteke, hala nola **keys.openpgp.org** zerbitzarian (ikus aurrerago).

Komando-lerroan GPG erabiliz zifratu diren fitxategiak bidaltzeko, nahikoa da emailari erantsi eta bidaltzea.

- Zifratu fitxategi hau eta bidali elkarri, **Konfidentzialtasuna**, **Osotasuna**, **Kautotzea** eta **Zapuztezintasuna** printzipioak lortzeko moduan.

> Arrazoitu zer egin behar izan duzuen horietako bakoitza lortzeko.

Konfidentzialtasuna: jasotzailearen gako publikoarekin zifratuz lortzen da, soilik berak deszifratu ahalko duelako bere gako pribatuarekin.
Autenticación eta No Repudio: igorlearen gako pribatuarekin zinatuz lortzen da, jasotzaileak igorlearen gako publikoa erabiltzen du konprobatzeko bera izan dela bidali duena.
Integritatea: firma digitalak hash kriptografiko bat du edukiarena, mezua aldatzen bada (nahiz eta bit bakarra izan), firmak ez du balioko.

```bash
# Cifrar y firmar simultáneamente EN BINARIO
gpg --encrypt --sign --recipient email_destinatario@ejemplo.com fitxategia.txt
```
```bash
#Cifrar, firmar y armor para que salga EN ASCII
gpg --armor --encrypt --sign --recipient email_destinatario@ejemplo.com fitxategia.txt 
```
## GPG gakoen gaineko konfiantza

Ikusi ahal izan duzuenez, oso erraza da gako-pare bat sortzea eta edozein izen jartzea. Ez da inolako egiaztapenik egiten. Beraz, pertsona batek sinatutako eta/edo zifratutako fitxategi bat jasotzen badugu, ezin dugu ziur egon pertsona hori benetan bera denik, baldin eta pertsona horri gako hori benetan berea den galdetzeko modurik ez badugu. Hala ere, badaude pertsona baten gakoetan konfiantza izateko mekanismoak, nahiz eta pertsona hori ez ezagutu edo harekin aldez aurretik hitz egin ez, gakoa benetan berea den egiaztatzeko.

- Talde bakoitzean ikasle bat “konfiantzazkotzat” izendatuko da; hau da, irakasleak konfiantza osoa izango du pertsona horrengan. Ikasle horrek bere gako publikoa irakasleari bidaliko dio. Taldeak lortu beharko du beste ikasleen gako publikoak irakasleari bidaltzean konfiantzazko gisa (`[full]`) agertzea **irakaslearen ordenagailuko gakoen giltzarrian**.

> Arrazoitu zer egin behar izan duzuen hori lortzeko.

1- Nire gako publikoa exportatuko dut berari pasatzeko
```bash
gpg --armor --export elaia.ort@gmail.com > elaia_publica.asc
```
2- Berak egin behar duena bere terminalean nire gakoa zinatzeko
```bash
# Importa tu clave
gpg --import elaia_publica.asc

# Firma tu clave con su clave privada
gpg --sign-key elaia.ort@gmail.com

# Exporta tu clave ya firmada por él/ella
gpg --armor --export elaia.ort@gmail.com > elaia_sinatuta.asc
```
3- Beraz, egin beharrekoa: Web of Trust modeloa erabili da. Irakasleak konfiantzazko ikasle bat duenez, ikasle horrek beste ikasleen gakoak zinatu behar ditu konfiantza transmititzeko. Irakasleak gako horiek bere konfiantzazko ikasleaz zinatuta jasotzen dituenean, bere sistemak automatikoki balidatuko ditu.

## Gako publikoen giltzarriak GPGn

Gakoak argitaratzeko eta bilatzeko modurik errazena [Keys OpenPGP](https://keys.openpgp.org/) bezalako zerbitzu bat erabiltzea da. Hura erabiltzeko, honako lerro hau gehitu behar zaio `/home/{usuario}/.gnupg/gpg.conf` fitxategiari:

```bash
keyserver hkps://keys.openpgp.org
```

- Konfiguratu GPGk **keys.openpgp.org**-ekin terminaletik lan egin dezan.
- Igo zure gakoa zerbitzarira, terminalean GPG erabiliz.
- Bilatu beste ikasleen gakoak eta irakaslearena, terminalean GPG erabiliz.
- Errepikatu aurreko ataleko **GPG gakoen gaineko konfiantza** ariketa, baina oraingoan erabili gako-zerbitzaria terminalaren bidez, gakoak irakasleari bidali beharrean (jakinarazi irakasleari konfiantzazko gakoak bila ditzan).

## SGSSI klaseko GPG gakoen giltzarri

Aurreko ataleko gakoen giltzarria birsortuko dugu, baina klaseko ikasleen gakoekin bakarrik eta eGela erabiliz. Horretarako, irakasleak konfiantza-kate bat definituko du, zenbait ikasle izendatuz, eta gainerako ikasleek beren gako publikoak igoko dituzte, konfiantza modu transitiboan bermatuz (konfiantzazko ikasleetatik hasita). Irakasleak katearen konfiantza egiaztatuko du gako guztiak inportatuz, baina konfiantza azkenari bakarrik emanez (Inportatzean, guztiek konfiantzazko gisa agertu beharko lukete irakaslearen ordenagailuan).

## GPG sinadurak

[Enigmail](http://www.enigmail.net/download) garatzaileen web-orrian bi fitxategi deskarga daitezke: Thunderbird-erako luzapena (`.xpi`) eta “GPG Signature” izeneko beste fitxategia.

> Zertarako balio du bigarren fitxategi horrek? Nola erabiltzen da?

Zertarako balio du? Bigarren fitxategi hori (.asc) jatorrizko fitxategiaren (.xpi) sinadura digitala da. Deskargatu dugun programa benetakoa dela (garatzaile ofizialek sortua) eta bidean inork ez duela aldatu edo kutsatu (osotasuna eta autentikotasuna) bermatzen du.   

Nola erabiltzen da? Bi fitxategiak karpeta berean izanda, terminalean honako komando hau exekutatuz egiaztatzen da:
```bash
gpg --verify enigmail.xpi.asc enigmail.xpi
```

GitHuben commit-ak GPG bidez sinatzeko aukera dago, commit horien segurtasuna eta trazabilitatea handitzeko. Irakasleak `6176ac9c479797c698b153c7750fa3e4421f445d` hash-a duen commit-a sinatu du, gaztelerazko apunteen biltegiko `develop` adarrekoa, [EHU-SGSSI-01](https://github.com/mikel-egana-aranguren/EHU-SGSSI-01) irakasgaiarena, honako gako publikoarekin batera sortutako gako pribatua erabiliz (`mikel.egana.aranguren@gmail.com`):

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
mDMEaMlpKBYJKwYBBAHaRw8BAQdA9BUe340yfVTGvu5htYNgujz5pGtx6GfIRP8h
CALZ+im0OE1pa2VslEVnYcOxYSBBcmFuZ3VyZW4gPG1pa2VsLmVnYW5hLmFyYW5n
dXJlbkBnbWFpbC5jb20+iJkEExYKAEEWIQQYFaxDxNCAFSKkZypj4GjUA79N7wUC
aMlpKAIbAwUJBaOagAULCQgHAgIiAgYVCgkICwIEFgIDAQIeBwIXgAAKCRBj4GjU
A79N75+fAQD75ya26vOiPsP18zWcclNbEqbt4f/260ycrRYsAoeNAgD/Wsa8GlSP
DnG2X1SC2GY8/X0rfcavzE3Ib4gJzoOkSQe4OARoyWkoEgorBgEEAZdVAQUBAQdA
4zlL3S3rbtPiUuPBscGteaVhYCRjmVuph+0KE/FUQUoDAQgHiH4EGBYKACYWIQQY
FaxDxNCAFSKkZypj4GjUA79N7wUCaMlpKAIbDAUJBaOagAAKCRBj4GjUA79N71q2
AP0W791v7y2QBsaxNuWlZqW/CNHamHJz1hr7tCWs/Jfa2wD9Gh1rszwCy6zXCNOv
hqLrPTy2euh/O45VyZSigvW+QgM=
=aYb8
-----END PGP PUBLIC KEY BLOCK-----
```

Commit-a GitHuben egiaztatuta gisa agertzen da (“Verified”). Zer esan nahi du horrek?
Commit bat GitHub-en "Verified" (Egiaztatua) gisa agertzeak esan nahi du GitHub-ek kriptografikoki egiaztatu duela commit horren egileak bere gako pribatu PGP/GPGa erabili zuela aldaketak sinatzeko, eta gako publiko bera bere GitHub kontuarekin lotuta dagoela.

![GitHub Commit](github_commit.png)

> Egiaztatu commit hori bera zure ordenagailu lokalean. Zein urrats egin behar dituzu?

Pausuak:
```bash
#Mikelen gpg publikoa inportatu
curl -s "https://github.com/mikel-egana-aranguren.gpg" | gpg --import

#Clone
git clone https://github.com/mikel-egana-aranguren/EHU-SGSSI-01.git
cd EHU-SGSSI-01
git checkout develop

#Egiaztatu
git verify-commit 6176ac9c479797c698b153c7750fa3e4421f445d
```

> Erabili zure GPG gakoak commit bat sinatzeko zure GitHub biltegi publikoetako batean, GitHuben ikustean “Verified” gisa ager dadin. Egiaztatu beste ikasleek sinatutako commit-ak.

1- GPG gakoa nire githubean sartu dut (new gpg key)
2- proba.txt aldatu dut commit-a egiteko
3- Commit egiteko pausu hauek jarraitu ditut
```bash
git add .
git commit -S -m "Commit sinatua probaldia"
git push origin main
```
4- Hasieran errore bat eman dit ezin zuelako interfazerik erabili pasahitza sartzeko, beraz komando hauek sartuz konpontzen da:
```bash
echo 'export GPG_TTY=$(tty)' >> ~/.bashrc
source ~/.bashrc
```
Eginda!
<img width="868" height="539" alt="image" src="https://github.com/user-attachments/assets/c67b2b14-7b4c-4724-bc32-2c9e15518535" />


## GPGren beste funtzionalitate batzuk

Garrantzitsua da zuen gakoak beste ekipo batzuetan erabiltzeko gai izatea, batez ere azterketari begira.

> Nola esportatzen da GPG gako bat beste ekipo batean erabili ahal izateko?

1- Biak exportatu behar dira
```bash
gpg --armor --export zure_emaila@adibidea.com > gako_publikoa.asc
gpg --armor --export-secret-keys zure_emaila@adibidea.com > gako_pribatua.asc
```
2- Biak importatu behar dira beste ordenagailuan (usb bidez eraman, adibidez)
```bash
gpg --import gako_pribatua.asc
gpg --import gako_publikoa.asc
```

Gerta daiteke gako bat konprometitzea.

> Nola baliogabetuko zenuke zure gakoa?

1- Baliogabetze ziurtagiri bat sortuz
```bash
gpg --output baliogabetzea.asc --gen-revoke zure_emaila@adibidea.com
```
2- Ziurtagiria inportatu
```bash
gpg --import baliogabetzea.asc
```
3- Gako zerbitzarira igorri besteek jakiteko (nahi bada)
```bash
gpg --keyserver hkps://keys.openpgp.org --send-keys ZURE_GAKOAREN_IDA
```

Nahiz eta haren funtzio nagusia zifraketa asimetrikoa izan, GPG zifratzeko ere erabil daiteke modu simetrikoan.

> Nola zifratuko zenuke dokumentu hau modu simetrikoan, eta zein urrats jarraituko zenituzke hartzaileak deszifratu ahal izan dezan?

1- Zifratu modu simetrikoan
```bash
gpg --symmetric --cipher-algo AES256 --armor fitxategia.txt
#GPGk pasahitz bat sartzeko eskatuko dizu eta fitxategia.txt.asc fitxategi cifratua sortuko du
```
2- Hartzaileak deszifratu ahal izateko jarraitu beharreko urratsak
 2.1- Pasahitza partekatu: Zifratzeko erabilitako pasahitza hartzaileari helarazi behar diozu kanal seguru independente bat erabiliz
 2.2- Fitxategia bidali: Zifratutako fitxategia (fitxategia.txt.asc) posta elektronikoz edo nahi duzun bidetik bidali.
 2.3-Hartzaileak deszifratzea: Hartzaileak komando hau exekutatuko du bere terminalean:
 ```bash
gpg --decrypt fitxategia.txt.asc > fitxategia.txt
#Sistemak pasahitza eskatuko dio, eta zuzen sartzean jatorrizko dokumentua berreskuratuko du
```

## RSA

Sortu RSA gako-pare bat OpenSSL erabiliz:

```bash
openssl genpkey -algorithm RSA -out gako.pem
```
`gako.pem` fitxategiak bi gakoak ditu; haren barne-egitura ikusteko:

```bash
openssl rsa -text -in gako.pem
```

Gako publikoa ateratzeko:

```bash
openssl rsa -pubout -in gako.pem -out gako_publikoa.pem
```

Zifratu mezu bat gako publikoarekin `openssl pkeyutl -encrypt` erabiliz. Deszifratu gako pribatuarekin eta egiaztatu mezuak bat datozela.

> RSA fitxategi txikietarako erabiltzen da. Nola inplementatuko zenuke zifraketa hibrido bat, AES erabiliz fitxategia modu simetrikoan zifratzeko eta RSA AES gakoa bera zifratzeko?
