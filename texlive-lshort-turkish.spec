# revision 15878
# category Package
# catalog-ctan /info/lshort/turkish
# catalog-date 2007-03-09 12:50:50 +0100
# catalog-license pd
# catalog-version 4.20
Name:		texlive-lshort-turkish
Version:	4.20
Release:	6
Summary:	Turkish introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/turkish
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-turkish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-turkish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A Turkish translation of Oetiker's (not so) short introduction.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-turkish/README
%doc %{_texmfdistdir}/doc/latex/lshort-turkish/lshort-tr.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-turkish/trlshort-src.zip

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.20-2
+ Revision: 753489
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.20-1
+ Revision: 718906
- texlive-lshort-turkish
- texlive-lshort-turkish
- texlive-lshort-turkish
- texlive-lshort-turkish

