cope='''El corría, nunca le enseñaron a andar,
se fue tras luces pálidas.
Ella huía de espejismos y horas de más.
Aeropuertos. Unos vienen, otros se van,
igual que Alicia sin ciudad.

El valor para marcharse,
el miedo a llegar.

Llueve en el canal, la corriente enseña
el camino hacia el mar.
Todos duermen ya.

Dejarse llevar suena demasiado bien.
Jugar al azar,
nunca saber dónde puedes terminar...
o empezar.

Un instante mientras los turistas se van.
Un tren de madrugada
consiguió trazar
la frontera entre siempre o jamás.



Llueve en el canal, la corriente enseña
el camino hacia el mar.
Todos duermen ya.

Dejarse llevar suena demasiado bien.
Jugar al azar,
nunca saber dónde puedes terminar...
o empezar.

Ella duerme tras el vendaval.
No se quitó la ropa.
Sueña con despertar
en otro tiempo y en otra ciudad.

Dejarse llevar suena demasiado bien.
Jugar al azar,
nunca saber dónde puedes terminar...
o empezar.'''
####################################
valiente='''
Tras de mí una escena y diez mil frases que repetir,
ya ves, lo que es no es.
Yo no voy a contar lo mejor, a ocultar lo peor,
me pongo el mejor chaqué.

No digo lo que digo,
hago lo que no hago,
al revés, al revés, porque
ser valiente no es sólo cuestión de suerte.

A veces no soy yo,
busco un disfraz mejor,
bailando hasta el apagón.
¡Disculpad mi osadía!

Tú también tienes que ver
que nunca tengo mi papel.
Nube gris, riega todo el jardín,
todo el jardín, todas las flores que no probé.

No olvido los sueños,
vuelvo a lo que no acabó,
no perdí, no perdí, porque
ser valiente no es sólo cuestión de verte.



A veces no soy yo,
busco un disfraz mejor,
bailando hasta el apagón.
¡Disculpad mi osadía!

Pensad que ya no estoy,
que el eco no es mi voz,
mejor aplaude y vámonos.
¡Qué termine esta función!

Tras de mí una escena y diez mil frases que repetir,
ya ves, lo que es no es.

A veces no soy yo,
busco un disfraz mejor,
bailando hasta el apagón.
¡Disculpad mi osadía!

Pensad que ya no estoy,
que el eco no es mi voz,
mejor aplaude y vámonos.
¡Qué termine esta función!

Deme la voz, deme la voz, deme la voz,
apuntador, deme la voz, deme la voz,
apuntador, deme la voz, deme la voz,
deme la voz, deme la voz, la voz ...
'''
##################################
marea='''
La marea me dejó arenas de plata,
que pondré en el reloj del tiempo que no pasa.
La marea me dejó islas inundadas,
donde atrapar con mi red una historia de piratas

Tu marea me dejó la piel cuarteada,
la miel en los labios,
las piernas enterradas.
La marea me dejó la piel cuarteada,
la miel en los labios,
las piernas enterradas.

La marea me dejó aromas de un barco,
algas tejidas en forma de desengaño.
La marea me dejó unas conchas sin nombre,
con que el niño hace un collar de un alfabeto que no entiende el hombre.

Tu marea me dejó la piel cuarteada,
la miel en los labios,
las piernas enterradas.
La marea me dejó la piel cuarteada,
la miel en los labios ,
las piernas enterradas.

La marea me dejó cangrejos helados,
agujas de hielo y un libro en blanco.
La marea me dejó los versos borrados.
la tinta, un borrón, un papel mojado

Tu marea me dejó la piel cuarteada,
la miel en los labios,
las piernas enterradas.
La marea me dejó la piel cuarteada,
la miel en los labios ,
las piernas enterradas.
'''
###############################################

def initials(cope):
    cope=cope.lower()
    cope=cope.replace('.',' ')
    cope=cope.replace('!','')
    cope=cope.replace('?','')
    cope=cope.replace('¡','')
    cope=cope.replace('¿','')  
    cope=cope.replace('\n',' ')
    cope=cope.replace(',',' ')
    copewords=cope.split(' ')
    copewords=[word for word in copewords if word!='']
    print(copewords)
    user_input=str(input('What word you wanna learn?')).lower()
    counter=0
    memo=[]
    window=len(user_input)
    while len(copewords)>counter+window:
        windowstr=''
        result=[]
        for i in range(window):
            result.append(copewords[counter+i])
            windowstr+=copewords[counter+i][0] #first letter of all words inside the window

        if windowstr==user_input:
            print(result,windowstr)
            return result
        counter+=1
    return []
    
songs=[cope,valiente,marea]
for song in songs:
    print(initials(song))      
