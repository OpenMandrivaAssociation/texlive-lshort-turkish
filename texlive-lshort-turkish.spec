%global tl_name lshort-turkish
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.20
Release:	%{tl_revision}.1
Summary:	Turkish introduction to LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/turkish
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-turkish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-turkish.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Turkish translation of Oetiker's (not so) short introduction.

