Name:		texlive-tpslifonts
Version:	42428
Release:	2
Summary:	A LaTeX package for configuring presentation fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texpower/tpslifonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
