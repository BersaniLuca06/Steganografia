dimQuad=60
altezzaImg=600
larghezzaImg=600
img=createImage(altezzaImg,larghezzaImg,RGB)        #Creazione immagine 
img.loadPixels()                                    #Caricamento dei pixel iniziali

def setup():
    size(altezzaImg,larghezzaImg)                   #Imposto la larghezza e la lunghezza della pagina iniziale 
    frase=[]
    frase= input('scrivi una frase')                #Importo una frase per poi trasformala in colori RGB e la creo
    creaImmagine(frase)

def input(message=''):
    from javax.swing import JOptionPane             #Importo la libreria Java che mi permette di inserire la frase
    return JOptionPane.showInputDialog(frame,message)

def creaImmagine(frase):
    loadPixels()                                    #Caricamento dei pixel precedentemente caricati
    Pixel=0
    i=0
    lunghezza=len(frase)                            #Diamo una lunghezza alla frase e dicaimo che finchè e se la variabile i è minore della lunghezza allora mi metterai dentro la variabile R 
                                                    #il primo carattere in i, altrimenti dentro la variabile R inseriamo il numero 255, il quale corrisponde ad un colore nel codice aschi    
                                                    #e faremo la stessa cosa per le altre variabili G e B aumentando, di volta in volta, la variabile i 
    while(i<lunghezza): 
        if(i<lunghezza): 
            R=ord(frase[i]) 
        else: 
            R=255
        if(i+1<lunghezza):
            G=ord(frase[i+1])
        else:
            G=255
        if(i+2<lunghezza):
            B=ord(frase[i+2])
        else:
            B=255
        i=i+3 
        for j in range(dimQuad):                   #Tramite questi cicli for (con j e k e la dimensione dei quadrati) andremo a caricare il primo pixel e di conseguenza ad assegnare il colore in r,g.b
            for k in range(dimQuad):
                pixels[Pixel+k+(larghezzaImg*j)] = color(R, G, B) 
        Pixel=Pixel+dimQuad
        if(Pixel%larghezzaImg==0):                 #Con questo if stabiliamo che il ciclo, se verificato, aggiungerà al pixel inizizale un altro pixel e stamperà infine i colori RGB                
            Pixel=Pixel+(larghezzaImg*(dimQuad-1))    
        print R                                  
        print G
        print B

    while ((Pixel/dimQuad)%larghezzaImg):           #Infine, con gli ultimi cicli, stabiliamo che se la frase supera la lunghezza stabilita si crea un altro quadrato dove la frase in eccesso nel  
                                                    #primo quadrato si immette nel secondo e cosi via fino alla fine della frase inserita. Infine stampiamo tutto e salviamo     
        for i in range(dimQuad):
            for j in range(dimQuad):
                pixels[Pixel+k+(larghezzaImg*j)]=color(255,255,255)
        Pixel=Pixel+dimQuad
        if (Pixel%larghezzaImg==0):
            Pixel=Pixel+larghezzaImg*(dimQuad-1)
    updatePixels()                 
    save("Steganografia.tiff")              
