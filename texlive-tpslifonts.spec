# revision 15878
# category Package
# catalog-ctan /macros/latex/exptl/texpower/tpslifonts
# catalog-date 2007-01-18 20:18:05 +0100
# catalog-license gpl
# catalog-version 0.6
Name:		texlive-tpslifonts
Version:	0.6
Release:	1
Summary:	A LaTeX package for configuring presentation fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/exptl/texpower/tpslifonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package aims to improve presentations in terms of font
readability, especially with maths. The standard cm math fonts
at large design sizes are difficult to read from far away,
especially at low resolutions and low contrast color choice.
Using this package leads to much better overall readability of
some font combinations. The package offers a couple of
'harmonising' combinations of text and math fonts from the
(distant) relatives of computer modern fonts, with a couple of
extras for optimising readability. Text fonts from computer
modern roman, computer modern sans serif, SliTeX computer
modern sans serif, computer modern bright, or concrete roman
are available, in addition to math fonts from computer modern
math, computer modern bright math, or Euler fonts. This package
is part of the TeXPower bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tpslifonts/tpslifonts.sty
%doc %{_texmfdistdir}/doc/latex/tpslifonts/00readme.txt
%doc %{_texmfdistdir}/doc/latex/tpslifonts/0install.txt
%doc %{_texmfdistdir}/doc/latex/tpslifonts/__TPslifonts.tex
%doc %{_texmfdistdir}/doc/latex/tpslifonts/slifontsexample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
