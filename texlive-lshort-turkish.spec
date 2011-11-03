# revision 15878
# category Package
# catalog-ctan /info/lshort/turkish
# catalog-date 2007-03-09 12:50:50 +0100
# catalog-license pd
# catalog-version 4.20
Name:		texlive-lshort-turkish
Version:	4.20
Release:	1
Summary:	Turkish introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/turkish
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-turkish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-turkish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A Turkish translation of Oetiker's (not so) short introduction.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-turkish/README
%doc %{_texmfdistdir}/doc/latex/lshort-turkish/lshort-tr.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-turkish/trlshort-src.zip
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
