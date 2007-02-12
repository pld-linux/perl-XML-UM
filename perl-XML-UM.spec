#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	UM
Summary:	XML::UM - convert UTF-8 strings to any encoding supported by XML::Encoding
Summary(pl.UTF-8):   XML::UM - konwersja łańcuchów z UTF-8 do dowolnego kodowania obsługiwanego przez XML::Encoding
Name:		perl-XML-UM
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c8de66145627b8ed3db27c72510b73d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Encoding
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XML::UM Perl module provides methods to convert UTF-8 strings to
any XML encoding that the XML::Encoding manpage supports.

%description -l pl.UTF-8
Moduł Perla XML::UM dostarcza metody do konwersji łańcuchów UTF-8 do
dowolnego kodowania XML obsługiwanego przez XML::Encoding.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/UM.pm
%{_mandir}/man3/*
