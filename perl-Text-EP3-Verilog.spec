#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	EP3-Verilog
Summary:	Text::EP3::Verilog perl module
Summary(pl.UTF-8):	Moduł perla Text::EP3::Verilog
Name:		perl-Text-EP3-Verilog
Version:	1.00
Release:	12
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f0a804e7aa348b44c6e23f42ae890ba
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Text-EP3
%endif
Requires:	perl-Text-EP3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::EP3::Verilog - Verilog extension for the EP3 preprocessor.

%description -l pl.UTF-8
Text::EP3::Verilog - rozszerzenie dla preprocesora EP3.

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
%dir %{perl_vendorlib}/Text/EP3
%{perl_vendorlib}/Text/EP3/Verilog.pm
%{perl_vendorlib}/auto/Text/EP3/Verilog
%{_mandir}/man3/*
