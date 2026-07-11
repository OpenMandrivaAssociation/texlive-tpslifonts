%global tl_name tpslifonts
%global tl_revision 42428

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	A LaTeX package for configuring presentation fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texpower/tpslifonts
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tpslifonts.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package aims to improve of font readability in presentations,
especially with maths. The standard cm maths fonts at large design sizes
are difficult to read from far away, especially at low resolutions and
low contrast color choice. Using this package leads to much better
overall readability of some font combinations. The package offers a
couple of 'harmonising' combinations of text and maths fonts from the
(distant) relatives of computer modern fonts, with a couple of extras
for optimising readability. Text fonts from computer modern roman,
computer modern sans serif, SliTeX computer modern sans serif, computer
modern bright, or concrete roman are available, in addition to maths
fonts from computer modern maths, computer modern bright maths, or Euler
fonts. The package is part of the TeXPower bundle.

