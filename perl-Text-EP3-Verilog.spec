%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	EP3-Verilog
Summary:	Text::EP3::Verilog perl module
Summary(pl):	Modu³ perla Text::EP3::Verilog
Name:		perl-Text-EP3-Verilog
Version:	1.00
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Text-EP3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::EP3::Verilog - Verilog extension for the EP3 preprocessor.

%description -l pl
Text::EP3::Verilog - rozszerzenie dla preprocesora EP3.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Text/EP3
%{perl_vendorlib}/Text/EP3/Verilog.pm
%{perl_vendorlib}/auto/Text/EP3/Verilog
%{_mandir}/man3/*
