#
# Conditional build:
%bcond_without tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	UM
Summary:	XML::UM - convert UTF-8 strings to any encoding supported by XML::Encoding
Summary(pl):	XML::UM - konwersja ³añcuchów z UTF-8 do dowolnego kodowania obs³ugiwanego przez XML::Encoding
Name:		perl-XML-UM
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e4c3fdd46e7ada0f9db326b493058d4d
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XML::UM Perl module provides methods to convert UTF-8 strings to
any XML encoding that the XML::Encoding manpage supports.

#%description -l pl

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
