README
======

You can read more about this API on
`weerlive <http://weerlive.nl/delen.php>`__

Further info is in Dutch, Het Weer in Nederland, door
`Surfcheck <http://surfcheck.info/>`__

**Fields** \* plaats: de locatie \* temp: actuele temperatuur \* gtemp:
gevoelstemperatuur \* samenv: omschrijving weersgesteldheid \* lv:
relatieve luchtvochtigheid \* windr: windrichting \* windms:
windsnelheid in meter per seconde \* winds: windkracht (Beaufort) \*
windk: Windsnelheid in knopen \* windkmh: Windsnelheid in km/h \*
luchtd: luchtdruk \* ldmmhg: luchtdruk in mm-kwikdruk \* dauwp: dauwpunt
\* zicht: zicht in km \* verw: korte dagverwachting \* sup: zon op \*
sunder: zon onder \* image: afbeeldingsnaam \* d1weer: Weericoon morgen
\* d1tmax: Maxtemp morgen \* d1tmin: Mintemp morgen \* d1windk:
Windkracht morgen (in Bft) \* d1windr: Windrichting morgen \*
d1neerslag: Neerslagkans morgen (%) \* d1zon: Zonkans morgen (%) \*
d2tmax: Maxtemp overmorgen \* d2tmin: Mintemp overmorgen \* d2weer:
Weericoon overmorgen \* d2windk: Windkracht overmorgen (in Bft) \*
d2windr: Windrichting overmorgen \* d2neerslag: Neerslagkans overmorgen
(%) \* d2zon: Zonkans overmorgen (%) \* alarm: Geldt er een
weerwaarschuwing voor deze regio of niet? \* alarmtxt: Als er sprake is
van een waarschuwing, verschijnt alarmtxt in de API. Hier lees je de
omschrijving van de weersituatie.

**De mogelijke iconen zijn:**

-  zonnig
-  bliksem
-  regen
-  buien
-  hagel
-  mist
-  sneeuw
-  bewolkt
-  halfbewolkt
-  zwaarbewolkt
-  nachtmist
-  helderenacht
-  wolkennacht

(Eventueel kun je hier meteen een set iconen met deze namen
`downloaden <http://weerlive.nl/items/iconen-weerlive.zip>`__, zodat je
gelijk aan de slag kunt. Deze iconen maken onderdeel uit van een grotere
open source set van 62 iconen, `deze vind je op
Github <https://github.com/jackd248/weather-iconic>`__)

Alle mogelijke windaanduidingen (16 stuks) zijn: \* Noord \* NNO \* NO
\* ONO \* Oost \* OZO \* ZO \* ZZO \* Zuid \* ZZW \* ZW \* WZW \* West
\* WNW \* NW \* NNW

In de verwachtingen kan ook de weergave VAR worden gebruikt \* voor
weinig wind uit variabele windrichtingen.

How do I get set up?
--------------------

-  Install this script with:

   -  pip3 py\_weerNL --upgrade (or pip py\_weerNL --upgrade )

-  ready to use it!

How do I use it
---------------

::

    from py_weernl import weerlive

    place = "wolphaartsdijk"

    w = weerLive()

    data = w.getData(place)

**Output :**

::

    {'liveweer': [{'d1windknp': '8', 'd2windk': '3', 'd0windr': 'NO', 'plaats': 'Goes', 'windr': 'NO', 'windk': '19.4', 'luchtd': '1023.2', 'd1weer': 'halfbewolkt', 'samenv': 'Licht bewolkt', 'd2neerslag': '10', 'verw': 'Zonnig en schraal. Vannacht lokaal matig vorst.', 'd1zon': '70', 'd2windr': 'NO', 'lv': '42', 'd2windkmh': '15', 'd1windk': '3', 'd0tmin': '-5', 'temp': '4.5', 'd0neerslag': '0', 'd1windms': '4', 'sunder': '18:17', 'image': 'halfbewolkt', 'd1tmax': '1', 'd1tmin': '-5', 'windms': '10', 'sup': '07:37', 'd2tmax': '1', 'd0windms': '7', 'gtemp': '-1.1', 'd0tmax': '3', 'd1windr': 'O', 'd2tmin': '-5', 'd1neerslag': '10', 'dauwp': '-8', 'd2windms': '4', 'd1windkmh': '15', 'winds': '5', 'd0windknp': '14', 'd2weer': 'bewolkt', 'd2windknp': '8', 'd0windk': '4', 'd0weer': 'zonnig', 'ldmmhg': '767', 'd0windkmh': '26', 'alarm': '0', 'd2zon': '20', 'windkmh': '36', 'd0zon': '93', 'zicht': '28'}]}

Thats all!!

Who do I talk to?
-----------------

-  Theodorus van der Sluijs (friends call me Theo)
-  theodorus@vandersluijs.nl

License
-------

Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

You are free to:
~~~~~~~~~~~~~~~~

-  Share — copy and redistribute the material in any medium or format
-  Adapt — remix, transform, and build upon the material

-The licensor cannot revoke these freedoms as long as you follow the
license terms.-

Under the following terms:
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Attribution — You must give appropriate credit, provide a link to the
   license, and indicate if changes were made. You may do so in any
   reasonable manner, but not in any way that suggests the licensor
   endorses you or your use.
-  NonCommercial — You may not use the material for commercial purposes.
-  ShareAlike — If you remix, transform, or build upon the material, you
   must distribute your contributions under the same license as the
   original.
