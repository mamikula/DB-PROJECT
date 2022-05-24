# Database Project - Marcin Mikuła, Dominik Grzesik

<!-- ## Description:
Web application allowing to book a place in port on a lake.

## Technology:
  - MongoDB
  - Django -->

<h2> Temat projektu</h2>
<p align ="center">Aplikacja internetowa, pozwalająca na rezerwację miejsca w wybranym porcie.</p>

<h2> Technologie</h2>
<ul>
  <li> Baza danych MongoDB Atlas</li>
  <li> Django Famework Frontedn i Backend </li>
</ul>
 
<h2> Funkcjonalności</h2>
<p align ="center">Aplikacja internetowa pozwala na rezerwację miejsca w wyszukanym porcie.</p> 

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)

<p font-size="10px" align ="center"> Rysunek 1: Lista wszystkich portów z opcją wyszukiwania po nazwie. </p> 
<br>
<p> Każdy port ma swoje sektory, których ofertę użytkownik otrzymuje po podaniu danych jachtu. Jachty mają określone wymiary: długość, głębokość i szerokość. Dodatkowo obowiązkowy do podania jest też typ jachtu: mieczowy bądź balastowy. Łodzi mieczowych nie dotyczy ograniczenie na głębokość, jako że miecz można schować. Zanurzenie łodzi balastowych, jako że jest stałe, może być zbyt duże i dana rezerwacja może nie być możliwa - w ofercie nie będzie sektorów z tą bądź mniejszą głębokością.  </p>

<br><br>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<p font-size="10px" align ="center"> Rysunek 2: Formularz na dane łodzi potrzebne do wyszukania dostępnych sektorów. </p> 

<br><br>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<p font-size="10px" align ="center"> Rysunek 3: Efekt wypełnienia formularza oraz wyszukania wyników. </p> 

<br>
 
<ol><h3>Rodzaje sektorów:</h3>
  <li>
    Pierwszy z nich, typu “równoległy”, to taki, do którego jachty cumują równolegle. Ograniczeniem jest długość sektora, w pewnym momencie następny jacht się już nie zmieści.
  </li>
  
  <li>
    Drugi typ to “prostopadły”, zawierający miejsca, w których jachty cumują prostopadle do pomostu. Ograniczeniem tutaj jest wspólna dla wszystkich miejsc danego sektora maksymalna szerokość łodzi. W momencie rezerwacji danego miejsca znika ono z oferty i nie można go zarezerwować.
    
 ![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<p font-size="10px" align ="center"> Rysunek 4: Dostępne miejsca w wybranym sektorze prostopadłym  </p> 
  </li>
  
  <li>
    Oba typy sektorów mają również określoną głębokość, czyli maksymalne zanurzenie jachtu.
  </li>
</ul>

<p>W momencie wybrania miejsca użytkownik zostaje poproszony o podanie danych potrzebnych do wykonania rezerwacji:</p>

<br>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<p font-size="10px" align ="center"> Rysunek 5: Formularz danych potrzebny do podania w momencie rezerwacji. </p> 
<br>

<p>W momencie wykonania rezerwacji klient dostaje obowiązkowy do zapisania bądź zapamiętania numer rezerwacji:</p>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<p font-size="10px" align ="center"> Rysunek 6: Komunikat z koniecznym do zapisania numerem rezerwacji. </p> 
<br>

<p align ="center">Będzie on potrzebny do podania w momencie próby znalezienia rezerwacji w zakładce rezerwacje: </p>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<p font-size="10px" align ="center"> Rysunek 7: Wyszukiwanie rezerwacji o danym numerze. </p> 
<br>
<br>

<ul><h3>Aktywne rezerwacje można:</h3>
  <li>edytować, tzn. zmieniać datę rozpoczęcia i zakończenia rezerwacji oraz usuwać, czyli anulować.
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<p font-size="10px" align ="center"> Rysunek 8: Opcje usuwania lub edytowania rezerwacji. </p> 
<br>
    
 ![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<p font-size="10px" align ="center"> Rysunek 9: Rezultat edycji wybranej rezerwacji.</p> 
<br>
    
  </li>
</ul>

 
<h2> Baza danych MongoDB Atlas </h2>

<p> Baza danych PortDB składa się z 3 kolekcji o przykładowych dokumentach: </p>

<p> Port z tablicą sektorów, z których każdy, jeśli typu prostopadłego, zawiera tablicę miejsc do rezerwacji: </p>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<p font-size="10px" align ="center"> Rysunek 9: Rezultat edycji wybranej rezerwacji.</p> 
<br>

<h3> Reservation </h3>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>

<h3> oraz Yacht </h3>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>

<h2> V. Django Framework </h2>
<p> Do bazy danych podpinamy się przez pymongo: </p>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>

<ol>
  <li> <h2> Widoki: </h2><br>
    
<p>views.port_list  - lista portów:</p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
<p>views.sectors - lista sektorów:</p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
<p>views.slots - list miejsc:</p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
<p>views.reserve - wykonywanie rezerwacji:</p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
<p>views.edit_reservation - edytowanie bądź usuwanie rezerwacji:</p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
<p>views.reservation - podgląd na rezerwację o danym numerze(to powinno być przed opcją edycji, ale w pdfie zostaje dziura na ¾ strony):</p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
  </li>
  
  <li> <h2> Formularze: </h2><br>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
  </li>
  
  <li> <h2> Routing: </h2><br>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
  </li>
  
  <li> <h2> Wyświetlanie informacji następuje w plikach .html: </h2><br>
    
<p> ports.html: </p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
<p> sectors.html: </p>

![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
<p> slots.html: </p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
<p> reservations.html: </p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
    
<p> results.html - w zależności od wykonanej akcji, dostajemy specjalny komunikat/informację, ostrzeżenie: </p>
    
![image](https://github.com/mamikula/CampaignForProducts/blob/master/Screens/ss1.png)
<br>
   
  </li>
</ol>
  














