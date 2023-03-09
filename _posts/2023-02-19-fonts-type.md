Fonts in LaTeX are characterized by four independent attributes:

Encoding
Family
Series
Shape

The encoding refers to the "output encoding"; commonly used ones are OT1 (classical TeX fonts) and T1 (Cork encoding for European languages), but also TS1 is found (Text Symbols); other encodings are T2A T2B T2C (for cyrillic), T3 (IPA glyphs), T4 (African languages) and T5 (Vietnamese).

The family attribute identifies a font family: cmr is the default Computer Modern, ptm is "Adobe Times New Roman", qcs is "TeX Gyre Schola" (cs is the two letter combination that refers to New Century Schoolbook or clones thereof).

The series is the "weight" of the font; it refers to both the thickness of the strokes and their width, so the letters can be m (for medium), bx (bold extended), b (bold), but also other series are found. Typical scalable fonts from the Postscript world have m and b weights (and bx is remapped to b).

The shape can be upright (n), italic (it), slanted (sl) or small capitals (sc). Some font families have also an "unslanted italic" variant (ui).

When LaTeX finds a new encoding+family combination it tries to read a font description file (for instance t1ptm.fd or t1qcs.fd) that contains in a convenient format the instructions for associating a "real font" to combinations of attributes. If the font description file doesn't exist, it's also possible to give explicitly these associations in the LaTeX document.

In some cases the combination of attributes doesn't point to an existent font. This is the case, for instance, of "T1/cmtt/bx/n" (Computer Modern Typewriter bold extended upright in T1 encoding). LaTeX can act differently in these cases:

if the .fd file defines a substitution rule, LaTeX follows the rule
if the .fd file doesn't tell anything useful, LaTeX uses some built-in rules
It would be quite long to describe the built-in rules (they are found in source2e.pdf). Let's examine two cases.

In the t1cmtt.fd file we find the line

\DeclareFontShape{T1}{cmtt}{bx}{n}{<->ssub*cmtt/m/n}{}
which means

if the T1/cmtt/bx/n combination is requested, silently change it into T1/cmtt/m/n.

In the t1qcs.fd file there is instead

\DeclareFontShape{T1}{qcs}{m}{sl}{<->sub * qcs/m/it}{}
which means

if the T1/qcs/m/sl combination is requested, change it into T1/qcs/m/it and warn the user (once).

Note that the encoding is never changed, because this might end up in printing unexpected characters.

The difference between the two cases is just an "s": ssub means "silently substitute", while sub means "substitute and warn" (the warning about this particular substitution is issued only once).

It's a developer's choice: the TeX Gyre people thought it best to warn a user about this substitution; there is no TeX Gyre Schola slanted font, so another one must be chosen.

For the most common attributes LaTeX has commands for setting them: \bfseries chooses the bx series attribute (actually it uses the macro \bfdefault); similarly \itshape chooses the shape attribute it (again, the reality is that \itdefault is used) and so on. Font developers can use arbitrarily many series and shape attributes. Some fonts have tens of possible choices.