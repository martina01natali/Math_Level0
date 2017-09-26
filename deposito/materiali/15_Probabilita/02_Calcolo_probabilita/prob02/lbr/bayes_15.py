"""
Esempi sulla probabilità
"""

def bayes_15(produzione1, probabilita_d1, produzione2, probabilita_d2):
    """
\begin{esempio}
Una fabbrica produce tondini di ferro grazie a due macchine. La prima 
macchina 
produce 1000 pezzi al giorno di cui il 3\% difettosi. la seconda produce 800 
pezzi al giorno di cui l'1\% difettosi. Se prendo a caso uno dei 1800 pezzi 
prodotti in un giorno e scopro che è difettoso, qual è la probabilità che 
provenga dalla prima macchina.
Consideriamo gli eventi:\\
$M_1$ ''il pezzo proviene dalla prima macchina''\\
$M_2$ ''il pezzo proviene dalla seconda macchina''\\
$D$ ''il pezzo è difettoso''\\
In base ai dati abbiamo:\\
$P(M_1)=\dfrac{1000}{1800}=\dfrac{5}{9}$
$P(M_2)=\dfrac{800}{1800}=\dfrac{4}{9}$
$P(D|M_1)=0,03$
$P(D|M_2)=0,01$
\end{esempio}
    """
    produzione_1_2 = produzione1 + produzione2
    probabilita_p1 = produzione1 / produzione_1_2
    probabilita_p2 = produzione2 / produzione_1_2
    probabilita_d_1_2 = (probabilita_d1 * probabilita_p1 +
                         probabilita_d2 * probabilita_p2)
    print(probabilita_d_1_2)
    probcond_1_d = probabilita_d1 * probabilita_p1 / probabilita_d_1_2
    return probcond_1_d
    

print(bayes_15(produzione1=1000, probabilita_d1=0.03,
               produzione2=800, probabilita_d2=0.01))
