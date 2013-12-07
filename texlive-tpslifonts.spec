# revision 27464
# category Package
# catalog-ctan /macros/latex/contrib/texpower/tpslifonts
# catalog-date 2012-04-27 17:14:22 +0200
# catalog-license gpl
# catalog-version 0.6
Name:		texlive-tpslifonts
Version:	0.6
Release:	6
Summary:	A LaTeX package for configuring presentation fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texpower/tpslifonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.source.tar.xz
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
math, computer modern bright math, or Euler fonts. The package
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
%doc %{_texmfdistdir}/doc/latex/tpslifonts/01install.txt
%doc %{_texmfdistdir}/doc/latex/tpslifonts/Makefile
%doc %{_texmfdistdir}/doc/latex/tpslifonts/slifontsexample.tex
#- source
%doc %{_texmfdistdir}/source/latex/tpslifonts/tpslifonts.dtx
%doc %{_texmfdistdir}/source/latex/tpslifonts/tpslifonts.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
