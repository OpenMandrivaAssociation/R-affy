%bcond_without bootstrap
%global packname  affy
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.38.1
Release:          1
Summary:          Methods for Affymetrix Oligonucleotide Arrays
Group:            Sciences/Mathematics
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/affy_1.38.1.tar.gz
Requires:         R-Biobase R-affyio R-Biobase R-BiocInstaller R-graphics
Requires:         R-grDevices R-methods R-preprocessCore R-stats R-utils
Requires:         R-zlibbioc R-tkWidgets
Requires:         R-BiocGenerics
%if %{without bootstrap}
Requires:         R-affydata
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Biobase
BuildRequires:    R-affyio R-Biobase R-BiocInstaller R-graphics
BuildRequires:    R-grDevices R-methods R-preprocessCore R-stats R-utils
BuildRequires:    R-zlibbioc R-tkWidgets
BuildRequires:    R-BiocGenerics
%if %{without bootstrap}
BuildRequires:    R-affydata
%endif

%description
The package contains functions for exploratory oligonucleotide array
analysis. The dependence on tkWidgets only concerns few convenience
functions. 'affy' is fully functional without it.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/tests


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.32.1-2
+ Revision: 778940
- Rebuild with proper dependencies
- Prepare to rebuild after breaking dependency cycle.

* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.32.1-1
+ Revision: 775753
- Import R-affy
- Import R-affy


