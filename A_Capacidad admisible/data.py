import pandas as pd
import numpy as np
import openpyxl as xl
import shutil
import os
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
#=============================================================================
from pylatex import Document, Package, NoEscape
from pylatex.utils import bold
#=============================================================================
class Datos:
    # Datos del proyecto
    pro = "Paquete R-10 Chancay"
    sub = "2527677"
    est = "DME Cantagallo"
    elab = "J.S."
    aprob = "H.A."
    fec = "24/03/2025"
    rev = "0A"
    file = None
    logo = None
    perf_image = None
    # Parametros de entrada
    coh, phi = 0.00, 0.00
    ydr, ymo = 0.00, 0.00
    mu = 0.00
    Es = 0.00
    B = 0.00
    L = 0.00
    Df = 0.00
    Ht = 0.00
    tma = 0.00
    yf = 0.00
    alp = 0.00
    Nc, Nq, Ny = 1.00, 1.00, 1.00
    ic, iq, iy = 1.00, 1.00, 1.00
    sc, sq, sy = 1.00, 1.00, 1.00
    pmax, qult, qadm = 1.00, 1.00, 1.00
    m, n, Is, If = 1.00, 1.00, 1.00, 1.00
    s_e, s_a = 1.00, 1.00

    u_se, u_sa = "cm", "cm"
    u_pm, u_qu, u_qa = "kPa", "kPa", "kPa"

    def gen_pdf(self):

        #Omitir si no hay ruta
        if not self.file:
            print("Ruta de archivo no definida.")
            return
        
        # Obtener nombre base sin extensión .pdf
        filename = os.path.splitext(os.path.basename(self.file))[0]
        outdir = os.path.dirname(self.file)

        #Definir las propiedades de la hoja
        geometry_options = {"right":"1cm", "left":"1cm", "top":"1cm", "bottom":"1cm", "landscape":True, "a4paper":True}
        doc = Document("reporte", geometry_options = geometry_options)
        doc.packages.append(Package("multirow"))
        doc.packages.append(Package("array"))
        doc.packages.append(Package("colortbl"))
        doc.packages.append(Package("xcolor", options="table"))
        doc.packages.append(Package("booktabs"))
        doc.packages.append(Package("graphicx"))
        doc.packages.append(Package("helvet"))
        doc.packages.append(Package("changepage"))
        doc.packages.append(Package("xcolor", options="table"))

        doc.preamble.append(NoEscape(r"\renewcommand{\familydefault}{\sfdefault}"))

        # Definir bloque del logo
        if self.logo:
            logo_block = r"""
            \multirow{3}{*}{
                \begin{minipage}[c][2cm][c]{0.15\textwidth}
                    \centering
                    \includegraphics[height=1.1cm,keepaspectratio]{""" + self.logo.replace("\\", "/") + r"""}
                \end{minipage}
            } &"""
        else:
            logo_block = r"""
            \multirow{3}{*}{
                \begin{minipage}[c][2cm][c]{0.15\textwidth}
                \end{minipage}
            } &"""

        # Definir imagen del perfil estratigrafico
        if self.logo:
            logo_block = r"""
            \multirow{3}{*}{
                \begin{minipage}[c][2cm][c]{0.15\textwidth}
                    \centering
                    \includegraphics[height=1.1cm,keepaspectratio]{""" + self.logo.replace("\\", "/") + r"""}
                \end{minipage}
            } &"""
        else:
            logo_block = r"""
            \multirow{3}{*}{
                \begin{minipage}[c][2cm][c]{0.15\textwidth}
                \end{minipage}
            } &"""


        #Definir el contenido
        strr = r"""
        \date{}
        \pagestyle{empty}
        \thispagestyle{empty}
        \setlength{\tabcolsep}{0pt}
        \setlength{\extrarowheight}{0pt}
        \begin{table}[htbp]
        \centering
        \begin{tabular}{|m{0.15\textwidth}|m{0.20\textwidth}|m{0.20\textwidth}|m{0.20\textwidth}|m{0.10\textwidth}|m{0.10\textwidth}|m{0.05\textwidth}|}
            \hline

            """ + logo_block + r"""
    
            \multicolumn{3}{c|}{
                \multirow{2}{*}{\parbox[c][1cm][c]{0.60\textwidth}{\centering \bfseries \fontsize{13}{14}\selectfont Memoria de calculo - Capacidad admisible}}
            } &

            \parbox[c][0.5cm][c]{0.10\textwidth}{\centering Elaborado:}&
            \parbox[c][0.5cm][c]{0.10\textwidth}{\centering """ + self.elab + r"""} &
            \multirow{3}{*}{\parbox[c][2cm][c]{0.05\textwidth}{\centering\bfseries \fontsize{16}{14} \selectfont 01}} \\

            \cline{5-6}

            & \multicolumn{3}{c|}{}
            \parbox[c][0.5cm][c]{0.20\textwidth}{}&
            \parbox[c][0.5cm][c]{0.10\textwidth}{\centering Aprobado:}&
            \parbox[c][0.5cm][c]{0.10\textwidth}{\centering """ + self.aprob + r"""} &\\
            
            \cline{2-6}

            &\parbox[c][0.5cm][c]{0.20\textwidth}{\centering Proyecto:} & 
            \parbox[c][0.5cm][c]{0.20\textwidth}{\centering Subproyecto:}&
            \parbox[c][0.5cm][c]{0.20\textwidth}{\centering Estructura:}&
            \parbox[c][0.5cm][c]{0.10\textwidth}{\centering Revisión:}&
            \parbox[c][0.5cm][c]{0.10\textwidth}{\centering """ + self.rev + r"""} &\\

            \cline{2-6}

            &\parbox[c][0.5cm][c]{0.20\textwidth}{\centering """ + self.pro + r"""} & 
            \parbox[c][0.5cm][c]{0.20\textwidth}{\centering """ + self.sub + r"""}&
            \parbox[c][0.5cm][c]{0.20\textwidth}{\centering """ + self.est + r"""}&
            \parbox[c][0.5cm][c]{0.10\textwidth}{\centering Fecha:}&
            \parbox[c][0.5cm][c]{0.10\textwidth}{\centering """ + self.fec + r"""} &\\

            \hline

            \multicolumn{2}{|c|}{
                \begin{minipage}[c][16.5cm][t]{0.35\textwidth}
                    \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                        \hline
                        \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{01.Parámetros de entrada}}} \\
                        \hline
                    \end{tabular}
                    \vspace{0.5em}
                    \begin{adjustwidth}{0.5em}{0.5em}
                        \begin{tabular}{m{0.10\textwidth} m{0.20\textwidth} m{0.15\textwidth} m{0.50\textwidth}}

                            \multicolumn{4}{l}{\textbf{Resumen de propiedades geotécnicas}} \\[0.5em]
                            \( c \):        & \hfill {\ """ + f"{self.coh:.2f}" + r"""} \hspace{1em}    & kPa & cohesión del suelo \\[0.25em]
                            \( \phi \):     & \hfill {\ """ + f"{self.phi:.2f}" + r"""} \hspace{1em}    & ° & ángulo de fricción del suelo \\[0.25em]
                            \( \gamma_d \): & \hfill {\ """ + f"{self.ydr:.2f}" + r"""} \hspace{1em}    & kN/m\(^3\) & peso unitario seco \\[0.25em]
                            \( \mu_s \):    & \hfill {\ """ + f"{self.mu:.2f}" + r"""} \hspace{1em}     & - & coeficiente de poisson \\[0.25em]
                            \( E_s\):       & \hfill {\ """ + f"{self.Es:.2f}" + r"""} \hspace{1em}     & kPa & módulo de elasticidad \\[0.5em]

                            \multicolumn{4}{l}{\textbf{Resumen de propiedades geométricas}} \\[0.5em]
                            \( B \):        & \hfill  {\ """ + f"{self.B:.2f}" + r"""} \hspace{1em}     & m & ancho de cimentación \\[0.25em]
                            \( L \):        & \hfill  {\ """ + f"{self.L:.2f}" + r"""} \hspace{1em}     & m & largo de cimentación \\[0.25em]
                            \( D_f \):      & \hfill  {\ """ + f"{self.Df:.2f}" + r"""} \hspace{1em}    & m & profundidad de cimentación \\[0.25em]
                            \( H \):        & \hfill  {\ """ + f"{self.Ht:.2f}" + r"""} \hspace{1em}    & m & profundidad de roca\\[0.5em]

                            \multicolumn{4}{l}{\textbf{Resumen de cargas}} \\[0.5em]
                            \( T \):        & \hfill  {\ """ + f"{self.tma:.2f}" + r"""} \hspace{1em}     & m & espesor promedio del DME \\[0.25em]
                            \( \gamma_f \): & \hfill  {\ """ + f"{self.yf:.2f}" + r"""} \hspace{1em}     & kN/m\(^3\) & peso unitario del relleno \\[0.25em]
                            \( \alpha \):   & \hfill  {\ """ + f"{self.alp:.2f}" + r"""} \hspace{1em}     & ° & angulo de inclinación de la carga \\[0.25em]
                        \end{tabular} 
                        \vspace{0.5em}
                    \end{adjustwidth}

                    \vspace{0.25em}
                    \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                        \hline
                        \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{02.Sección típica}}} \\
                        \hline
                    \end{tabular}
                    \vspace{0.25em}
                    \begin{center}
                        \centering
                    \end{center}
                \end{minipage}
            } &

            \multicolumn{2}{c}{
                \begin{minipage}[c][16.5cm][t]{0.40\textwidth}
                    \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                        \hline
                        \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{03.Cálculos intermedios}}} \\
                        \hline
                    \end{tabular}
                    \vspace{0.5em}

                    \begin{adjustwidth}{0.5em}{0.5em}

                        \begin{tabular}{m{0.33\textwidth} m{0.33\textwidth} m{0.33\textwidth}}

                            \multicolumn{3}{l}{\textbf{Factores de carga}} \\[0.5em]
                            \parbox{\linewidth}{\centering \( N_c \)} & 
                            \parbox{\linewidth}{\centering \( N_q \)} & 
                            \parbox{\linewidth}{\centering \( N_{\gamma} \)} \\[0.25em]
                            \parbox{\linewidth}{\centering {\ """ + f"{self.Nc:.2f}" + r"""}} & 
                            \parbox{\linewidth}{\centering {\ """ + f"{self.Nq:.2f}" + r"""}} & 
                            \parbox{\linewidth}{\centering {\ """ + f"{self.Ny:.2f}" + r"""}} \\[1em]

                            \multicolumn{3}{l}{\textbf{Factores de forma}} \\[0.5em]
                            \parbox{\linewidth}{\centering \( s_c \)} & 
                            \parbox{\linewidth}{\centering \( s_q \)} & 
                            \parbox{\linewidth}{\centering \( s_{\gamma} \)} \\[0.25em]
                            \parbox{\linewidth}{\centering {\ """ + f"{self.sc:.2f}" + r"""}} & 
                            \parbox{\linewidth}{\centering {\ """ + f"{self.sq:.2f}" + r"""}} & 
                            \parbox{\linewidth}{\centering {\ """ + f"{self.sy:.2f}" + r"""}} \\[1em]

                            \multicolumn{3}{l}{\textbf{Factores de inclinación de la carga}} \\[0.5em]
                            \parbox{\linewidth}{\centering \( i_c \)} & 
                            \parbox{\linewidth}{\centering \( i_q \)} & 
                            \parbox{\linewidth}{\centering \( i_{\gamma} \)} \\[0.25em]
                            \parbox{\linewidth}{\centering {\ """ + f"{self.ic:.2f}" + r"""}} & 
                            \parbox{\linewidth}{\centering {\ """ + f"{self.iq:.2f}" + r"""}} & 
                            \parbox{\linewidth}{\centering {\ """ + f"{self.iy:.2f}" + r"""}} \\[1em]

                        \end{tabular} 
                    \end{adjustwidth}
                    \vspace{0.5em}
                    \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                        \hline
                        \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{04.Presión máxima en la fundación}}} \\
                        \hline
                    \end{tabular}
                    \vspace{0.5em}
                    \begin{adjustwidth}{0.5em}{0.5em}

                        \begin{tabular}{m{0.10\textwidth} m{0.20\textwidth} m{0.15\textwidth} m{0.50\textwidth}}

                            \multicolumn{4}{l}{\textbf{Formula de presión máxima}} \\[0.5em]
                            \multicolumn{4}{c}{
                                $p_{max} = T \gamma_f$
                            } \\[1em]

                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}\( p_{max} \):} &
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.pmax + r"""}} &
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.u_pm + r"""}} &
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}presión máxima en la fundación} \\

                        \end{tabular} 
                    \end{adjustwidth}
                    \vspace{1em}
                    \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                        \hline
                        \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{05.Capacidad ultima y admisible}}} \\
                        \hline
                    \end{tabular}
                    \vspace{0.5em}
                    \begin{adjustwidth}{0.5em}{0.5em}
                        \begin{tabular}{m{0.10\textwidth} m{0.20\textwidth} m{0.15\textwidth} m{0.50\textwidth}}
                            \multicolumn{4}{l}{\textbf{Formula de capacidad última}} \\[0.5em]
                            \multicolumn{4}{c}{
                                $q_{ult} = c N_c s_c i_c + q N_q s_q i_q + 0.5 \gamma B N_\gamma s_\gamma i_\gamma$
                            } \\[1em]
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}\( q_{ult} \):} &
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.qult + r"""}} &
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.u_qu + r"""}} &
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}capacidad ultima} \\
                            \\[0.25em]
                            \multicolumn{4}{l}{\textbf{Formula de capacidad admisible}} \\[1em]
                            \multicolumn{4}{c}{
                                $q_{adm} = \frac{q_{ult}}{F_s}$
                            } \\[1em]
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}\( q_{adm} \):} &
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.qadm + r"""}} &
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.u_qa + r"""}} &
                            \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}capacidad admisible} \\

                        \end{tabular} 
                    \end{adjustwidth}
                \end{minipage}
            } &

            \multicolumn{3}{|c|}{
                \begin{minipage}[c][16.5cm][t]{0.25\textwidth}

                    \begin{tabular}{>{\columncolor[HTML]{A7D8FF}}m{1.0\textwidth}}
                        \hline
                        \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{Perfil estratigrafico}}} \\
                        \hline
                    \end{tabular}
                    \vspace{0.5em}

                    \begin{adjustwidth}{0.5em}{0.5em}
                        \begin{tabular}{m{1.00\textwidth}}
                            \begin{minipage}[c][11.02cm][c]{1\textwidth}
                                \begin{center}
                                    \includegraphics[height=10cm, width=0.9\textwidth, keepaspectratio]{""" + self.perf_image.replace("\\", "/") + r"""}
                                \end{center}                            
                            \end{minipage} \\[2em]
                        \end{tabular}
                    \end{adjustwidth}
                    
                    
                    \begin{tabular}{>{\columncolor[HTML]{A7D8FF}}m{1.0\textwidth}}
                        \hline
                        \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{Verificación de capacidad admisible}}} \\
                        \hline
                    \end{tabular}
                    \begin{adjustwidth}{0.5em}{0.5em}
                        \vspace{1em}
                        \parbox{0.95\textwidth}{
                            Se verifica la capacidad admisible comparandola con la presión máxima ejercida
                        }\\[1em]

                        \begin{tabular}{m{0.40\textwidth} m{0.20\textwidth} m{0.40\textwidth}}

                            \parbox{\linewidth}{\centering \( p_{max} \)} & 
                            \parbox{\linewidth}{\centering \( < \)} & 
                            \parbox{\linewidth}{\centering \( q_{adm} \)} \\[0.25em]
                            \parbox{\linewidth}{\centering {\ """ + self.pmax + " " + self.u_pm + r"""}} & 
                            \parbox{\linewidth}{\centering \( < \)} & 
                            \parbox{\linewidth}{\centering {\ """ + self.qadm + " " + self.u_qa + r"""}} \\[0.5em]

                        \end{tabular}                                         
                        \vspace{0.5em}
                    \end{adjustwidth}

                    \begin{tabular}{>{\columncolor[HTML]{E2F7E1}}m{1.0\textwidth}}
                        \hline
                        \parbox[c][0.76cm][c]{1.0\textwidth}{\centering{\textbf{Cumple}}} \\
                        \hline
                    \end{tabular}
                \end{minipage}    
            } \\

            \hline
        \end{tabular}
        \end{table}
        """

        #Definir el contenido
        strr2 = r"""
            \date{}
            \pagestyle{empty}
            \thispagestyle{empty}
            \setlength{\tabcolsep}{0pt}
            \setlength{\extrarowheight}{0pt}
            \begin{table}[htbp]
            \centering
            \begin{tabular}{|m{0.15\textwidth}|m{0.20\textwidth}|m{0.20\textwidth}|m{0.20\textwidth}|m{0.10\textwidth}|m{0.10\textwidth}|m{0.05\textwidth}|}
                \hline

                """ + logo_block + r"""
        
                \multicolumn{3}{c|}{
                    \multirow{2}{*}{\parbox[c][1cm][c]{0.60\textwidth}{\centering \bfseries \fontsize{13}{14}\selectfont Memoria de calculo - Asentamientos elasticos}}
                } &

                \parbox[c][0.5cm][c]{0.10\textwidth}{\centering Elaborado:}&
                \parbox[c][0.5cm][c]{0.10\textwidth}{\centering """ + self.elab + r"""} &
                \multirow{3}{*}{\parbox[c][2cm][c]{0.05\textwidth}{\centering\bfseries \fontsize{16}{14} \selectfont 02}} \\

                \cline{5-6}

                & \multicolumn{3}{c|}{}
                \parbox[c][0.5cm][c]{0.20\textwidth}{}&
                \parbox[c][0.5cm][c]{0.10\textwidth}{\centering Aprobado:}&
                \parbox[c][0.5cm][c]{0.10\textwidth}{\centering """ + self.aprob + r"""} &\\
                
                \cline{2-6}

                &\parbox[c][0.5cm][c]{0.20\textwidth}{\centering Proyecto:} & 
                \parbox[c][0.5cm][c]{0.20\textwidth}{\centering Subproyecto:}&
                \parbox[c][0.5cm][c]{0.20\textwidth}{\centering Estructura:}&
                \parbox[c][0.5cm][c]{0.10\textwidth}{\centering Revisión:}&
                \parbox[c][0.5cm][c]{0.10\textwidth}{\centering """ + self.rev + r"""} &\\

                \cline{2-6}

                &\parbox[c][0.5cm][c]{0.20\textwidth}{\centering """ + self.pro + r"""} & 
                \parbox[c][0.5cm][c]{0.20\textwidth}{\centering """ + self.sub + r"""}&
                \parbox[c][0.5cm][c]{0.20\textwidth}{\centering """ + self.est + r"""}&
                \parbox[c][0.5cm][c]{0.10\textwidth}{\centering Fecha:}&
                \parbox[c][0.5cm][c]{0.10\textwidth}{\centering """ + self.fec + r"""} &\\

                \hline

                \multicolumn{2}{|c|}{
                    \begin{minipage}[c][16.5cm][t]{0.35\textwidth}
                        \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                            \hline
                            \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{01.Parámetros de entrada}}} \\
                            \hline
                        \end{tabular}
                        \vspace{0.5em}
                        \begin{adjustwidth}{0.5em}{0.5em}
                            \begin{tabular}{m{0.10\textwidth} m{0.20\textwidth} m{0.15\textwidth} m{0.50\textwidth}}

                                \multicolumn{4}{l}{\textbf{Resumen de propiedades geotécnicas}} \\[0.5em]
                                \( c \):        & \hfill {\ """ + f"{self.coh:.2f}" + r"""} \hspace{1em}    & kPa & cohesión del suelo \\[0.25em]
                                \( \phi \):     & \hfill {\ """ + f"{self.phi:.2f}" + r"""} \hspace{1em}    & ° & ángulo de fricción del suelo \\[0.25em]
                                \( \gamma_d \): & \hfill {\ """ + f"{self.ydr:.2f}" + r"""} \hspace{1em}    & kN/m\(^3\) & peso unitario seco \\[0.25em]
                                \( \mu_s \):    & \hfill {\ """ + f"{self.mu:.2f}" + r"""} \hspace{1em}     & - & coeficiente de poisson \\[0.25em]
                                \( E_s\):       & \hfill {\ """ + f"{self.Es:.2f}" + r"""} \hspace{1em}     & kPa & módulo de elasticidad \\[0.5em]

                                \multicolumn{4}{l}{\textbf{Resumen de propiedades geométricas}} \\[0.5em]
                                \( B \):        & \hfill  {\ """ + f"{self.B:.2f}" + r"""} \hspace{1em}     & m & ancho de cimentación \\[0.25em]
                                \( L \):        & \hfill  {\ """ + f"{self.L:.2f}" + r"""} \hspace{1em}     & m & largo de cimentación \\[0.25em]
                                \( D_f \):      & \hfill  {\ """ + f"{self.Df:.2f}" + r"""} \hspace{1em}    & m & profundidad de cimentación \\[0.25em]
                                \( H \):        & \hfill  {\ """ + f"{self.Ht:.2f}" + r"""} \hspace{1em}    & m & profundidad de roca\\[0.5em]

                                \multicolumn{4}{l}{\textbf{Resumen de cargas}} \\[0.5em]
                                \( T \):        & \hfill  {\ """ + f"{self.tma:.2f}" + r"""} \hspace{1em}     & m & espesor promedio del DME \\[0.25em]
                                \( \gamma_f \): & \hfill  {\ """ + f"{self.yf:.2f}" + r"""} \hspace{1em}     & kN/m\(^3\) & peso unitario del relleno \\[0.25em]
                                \( \alpha \):   & \hfill  {\ """ + f"{self.alp:.2f}" + r"""} \hspace{1em}     & ° & angulo de inclinación de la carga \\[0.25em]
                            \end{tabular} 
                            \vspace{0.5em}
                        \end{adjustwidth}

                        \vspace{0.25em}
                        \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                            \hline
                            \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{02.Sección típica}}} \\
                            \hline
                        \end{tabular}
                        \vspace{0.25em}
                        \begin{center}
                            \centering
                        \end{center}
                    \end{minipage}
                } &

                \multicolumn{2}{c}{
                    \begin{minipage}[c][16.5cm][t]{0.40\textwidth}
                        \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                            \hline
                            \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{03.Cálculos intermedios}}} \\
                            \hline
                        \end{tabular}
                        \vspace{0.5em}

                        \begin{adjustwidth}{0.5em}{0.5em}

                            \begin{tabular}{m{0.5\textwidth} m{0.5\textwidth}}

                                \multicolumn{2}{l}{\textbf{Relacion geometrica m y n}} \\[0.5em]
                                \parbox{\linewidth}{\centering \( m \)} & 
                                \parbox{\linewidth}{\centering \( n \)} \\ 
                                \parbox{\linewidth}{\centering {\ """ + f"{self.m:.2f}" + r"""}} & 
                                \parbox{\linewidth}{\centering {\ """ + f"{self.n:.2f}" + r"""}} \\[1em]

                                \multicolumn{2}{l}{\textbf{Factores de forma y profundidad}} \\[0.5em]
                                \parbox{\linewidth}{\centering \( I_s \)} & 
                                \parbox{\linewidth}{\centering \( I_f \)} \\ 
                                \parbox{\linewidth}{\centering {\ """ + f"{self.Is:.2f}" + r"""}} & 
                                \parbox{\linewidth}{\centering {\ """ + f"{self.If:.2f}" + r"""}} \\[1em]

                            \end{tabular} 
                        \end{adjustwidth}
                        \vspace{0.5em}
                        \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                            \hline
                            \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{04.Presión máxima en la fundación}}} \\
                            \hline
                        \end{tabular}
                        \vspace{0.5em}
                        \begin{adjustwidth}{0.5em}{0.5em}

                            \begin{tabular}{m{0.10\textwidth} m{0.20\textwidth} m{0.15\textwidth} m{0.50\textwidth}}

                                \multicolumn{4}{l}{\textbf{Formula de presión máxima}} \\[0.5em]
                                \multicolumn{4}{c}{
                                    $q_o = T \gamma_f$
                                } \\[1em]

                                {\rule{0pt}{2.5ex}\( q_o \):} &
                                {\rule{0pt}{2.5ex}{\ """ + self.pmax + r"""}} &
                                {\rule{0pt}{2.5ex}{\ """ + self.u_pm + r"""}} &
                                {\rule{0pt}{2.5ex}presión máxima en la fundación} \\

                            \end{tabular} 
                        \end{adjustwidth}
                        \vspace{1em}
                        \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                            \hline
                            \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{05.Asentamiento elástico}}} \\
                            \hline
                        \end{tabular}
                        \vspace{1em}
                        \begin{adjustwidth}{0.5em}{0.5em}
                            \begin{tabular}{m{0.10\textwidth} m{0.20\textwidth} m{0.15\textwidth} m{0.50\textwidth}}
                                \multicolumn{4}{l}{\textbf{Formula de asentamiento elástico}} \\[1em]
                                \multicolumn{4}{c}{
                                    $S_e = q_o (\alpha B') \frac{1-\mu_s^2}{E_s} I_s I_f$
                                } \\[1em]
                                \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}\( S_e \):} &
                                \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.s_e + r"""}} &
                                \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.u_se + r"""}} &
                                \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}asentamiento elastico} \\[0.25em]

                            \end{tabular} 
                        \end{adjustwidth}
                       \vspace{1em}
                        \begin{tabular}{>{\columncolor[HTML]{EFEFEF}}m{1.0\textwidth}}
                            \hline
                            \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{06.Asentamiento admisible}}} \\
                            \hline
                        \end{tabular}
                        \vspace{1em}
                        \begin{adjustwidth}{0.5em}{0.5em}
                            \begin{tabular}{m{0.10\textwidth} m{0.20\textwidth} m{0.15\textwidth} m{0.50\textwidth}}
                                \multicolumn{4}{l}{\textbf{Formula de asentamiento admisible}} \\[1em]
                                \multicolumn{4}{c}{
                                    $S_adm = 0.01 T$
                                } \\[1em]
                                \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}\( S_{adm} \):} &
                                \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.s_a + r"""}} &
                                \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}{\ """ + self.u_sa + r"""}} &
                                \cellcolor[HTML]{2E3A59}\textcolor{white}{\rule{0pt}{2.5ex}asentamiento admisible} \\[0.25em]

                            \end{tabular} 
                        \end{adjustwidth}                        

                    \end{minipage}
                } &

                \multicolumn{3}{|c|}{
                    \begin{minipage}[c][16.5cm][t]{0.25\textwidth}

                        \begin{tabular}{>{\columncolor[HTML]{A7D8FF}}m{1.0\textwidth}}
                            \hline
                            \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{Perfil estratigrafico}}} \\
                            \hline
                        \end{tabular}
                        \vspace{0.5em}



                        \begin{adjustwidth}{0.5em}{0.5em}
                            \begin{tabular}{m{1.00\textwidth}}
                                \begin{minipage}[c][11.02cm][c]{1\textwidth}
                                    \begin{center}
                                        \includegraphics[height=10cm, width=0.9\textwidth, keepaspectratio]{""" + self.perf_image.replace("\\", "/") + r"""}
                                    \end{center}
                                \end{minipage} \\[2em]
                            \end{tabular}
                        \end{adjustwidth}
                        
                        
                        \begin{tabular}{>{\columncolor[HTML]{A7D8FF}}m{1.0\textwidth}}
                            \hline
                            \parbox[c][0.5cm][c]{1.0\textwidth}{\centering{\textbf{Verificación del asentamiento tolerable}}} \\
                            \hline
                        \end{tabular}
                        \begin{adjustwidth}{0.5em}{0.5em}
                            \vspace{1em}
                            \parbox{0.95\textwidth}{
                                Se verifica el asentamiento elástico, comparandolo con el asentamiento admisible.
                            }\\[1em]

                            \begin{tabular}{m{0.33\textwidth} m{0.33\textwidth} m{0.33\textwidth}}

                                \parbox{\linewidth}{\centering \( s_e \)} & 
                                \parbox{\linewidth}{\centering \( < \)} & 
                                \parbox{\linewidth}{\centering \( s_{adm} \)} \\[0.25em]
                                \parbox{\linewidth}{\centering {\ """ + self.s_e + " " + self.u_se + r"""}} & 
                                \parbox{\linewidth}{\centering \( < \)} & 
                                \parbox{\linewidth}{\centering {\ """ + self.s_a + " " + self.u_sa + r"""}} \\[0.5em]

                            \end{tabular}                                         
                            \vspace{0.5em}
                        \end{adjustwidth}

                        \begin{tabular}{>{\columncolor[HTML]{E2F7E1}}m{1.0\textwidth}}
                            \hline
                            \parbox[c][0.76cm][c]{1.0\textwidth}{\centering{\textbf{Cumple}}} \\
                            \hline
                        \end{tabular}
                    \end{minipage}    
                } \\

                \hline
            \end{tabular}
            \end{table}
        """

        doc.append(NoEscape(strr))  
        doc.append(NoEscape(strr2))  
        doc.generate_pdf(filepath=os.path.join(outdir, filename), compiler="pdflatex", clean=True)

#=============================================================================
def load_factor(phi):
    rad = phi*np.pi/180
    if rad == 0:
        Nq,Ny = 0, 0
        Nc = 5.14
    else:
        Nq = (np.exp(np.pi*np.tan(rad)))*((np.tan(0.25*np.pi+0.5*rad))**2)
        Nc = (Nq-1)/np.tan(rad)
        Ny = (Nq-1)*np.tan(1.4*rad)
    return [Nc,Nq,Ny]

def shape_factor(B,L):
    Sc = 1+0.2*B/L
    Sq = 1
    Sy = 1-0.2*B/L
    return [Sc,Sq,Sy]

def inclination_factor(alpha,phi):
    ic = (1-alpha/90)**2
    iq = ic
    if phi ==0:
        iy = 1
    else:
        iy = (1-alpha/phi)**2
    return [ic,iq,iy]

def ult_bearing(c,B,Df,N,S,I,y1,y2):
    qult = N[0]*S[0]*I[0]*c+N[1]*S[1]*I[1]*Df*y1+0.5*B*y2*N[2]*S[2]*I[2]
    return qult

def point_factor(type, B, L, Df, Ht):
    if type == "Center":
        alpha = 4
        m = L/B
        n = 2*(Ht-Df)/B
        b = B/2
    elif type == "Corner":
        alpha = 1
        m = L/B
        n = (Ht-Df)/B
        b = B
    return [alpha,m,n,b]

def set_factor(u,m,n,B,L,Df):
    A0 = m * np.log(((1+np.sqrt(m**2+1))*(np.sqrt(m**2+n**2)))/(m*(1+np.sqrt(m**2+n**2+1))))
    A1 = np.log(((m+np.sqrt(m**2+1))*(np.sqrt(1+n**2)))/(m+np.sqrt(m**2+n**2+1)))
    A2 = (m)/(n*(np.sqrt(m**2+n**2+1)))
    F1 = (A0 + A1)/ np.pi
    F2 = 0.5 * np.atan(A2) * n/ np.pi
    Is = F1 + F2*(1-2*u)/(1-u)
    If = (1.001+1.194*Df/B+0.842*L/B+7.63*u)/(1+3.738*Df/B+0.839*L/B+7.3*u)
    return [Is,If]

def create_profile(df, gw_level, state):
    fig, ax = plt.subplots(figsize=(6, 12))

    Hmax = max(df["Depth"])

    df = pd.DataFrame(df)

    df["espesor"] = df["Depth"].diff()          #Diferencia entre datos continuos
    h_inicial = df["Depth"][0]                   #Espesor inicial
    df.loc[df.index[0], "espesor"] = h_inicial 

    # Diccionario de estilos para cada tipo de suelo
    material_styles = {
        "Clay": {'color': '#9ACD32', 'hatch': "/", 'alpha': 0.2},
        "Lime": {'color': '#FFC0CB', 'hatch': "|", 'alpha': 1.0},
        "Sand": {'color': '#BDB76B', 'hatch': "oo", 'alpha': 1.0},
        "Gravel": {'color': '#F0E68C', 'hatch': "O.", 'alpha': 1.0},
        "Rock": {'color': '#E6E6FA', 'hatch': ".", 'alpha': 1.0},
        "Fract. Rock": {'color': '#778899', 'hatch': ".", 'alpha': 1.0}
    }
    # Materiales usados (sin duplicados)
    used_materials = set(df["Clasification"])
    
    # Graficar estratos
    for i in range(len(df)):
        sucs = df["Clasification"].iloc[i]
        style = material_styles.get(sucs, {})
        
        p = ax.bar(1, df["espesor"].iloc[i],
                  bottom=df["Depth"].iloc[i]-df["espesor"].iloc[i],
                  edgecolor="gray",
                  **style)

    # Agregar el nivel freático como línea horizontal
    if state == True:
        ax.axhline(y=gw_level, color='blue', linestyle='--', linewidth=2, alpha=0.7)

    # Detalles de lso garficos
    ax.set_ylabel("Depth", fontsize = 20)
    ax.set_ylim(0,Hmax)
    ax.invert_yaxis()
    ax.margins(x=0)
    ax.tick_params(axis="x",which="both",bottom=False,top=False,labelbottom=False)
    ax.tick_params(axis="y", labelsize=20)

    # Crear leyenda solo con lo usado
    legend_elements = []
    
    # Agregar materiales usados
    for material in used_materials:
        if material in material_styles:
            style = material_styles[material].copy()
            facecolor = style.pop("color", "gray")
            legend_elements.append(
                plt.Rectangle((0, 0), 1, 1, facecolor=facecolor, edgecolor='gray', **style, label=material)
            )
            
    # Agregar nivel freático a la leyenda
    if state == True:
        legend_elements.append(
            plt.Line2D([0], [0], color='blue', linestyle='--', linewidth=2, 
                    label=f'Nivel freático ({gw_level} m)')
        )
    
    # Mostrar leyenda
    ax.legend(handles=legend_elements, title="Elementos", title_fontsize=20, 
             fontsize = 20, bbox_to_anchor=(0.5, -0.05), loc='upper center')
    

    fig.tight_layout()

    return fig  # Devuelve un objeto plt.Figure
#=============================================================================

