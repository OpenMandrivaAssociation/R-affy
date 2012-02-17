%bcond_with bootstrap
%global packname  affy
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.32.1
Release:          2
Summary:          Methods for Affymetrix Oligonucleotide Arrays
Group:            Sciences/Mathematics
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-Biobase 
Requires:         R-affyio R-Biobase R-BiocInstaller R-graphics R-grDevices R-methods R-preprocessCore R-stats R-utils R-zlibbioc 
%if %{with bootstrap}
Requires:         R-tkWidgets
%else
Requires:         R-tkWidgets R-affydata 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Biobase
BuildRequires:    R-affyio R-Biobase R-BiocInstaller R-graphics R-grDevices R-methods R-preprocessCore R-stats R-utils R-zlibbioc 
%if %{with bootstrap}
BuildRequires:    R-tkWidgets
%else
BuildRequires:    R-tkWidgets R-affydata 
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
