%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	EP3-Verilog
Summary:	Text-EP3-Verilog perl module
Summary(pl):	Modu³ perla Text-EP3-Verilog
Name:		perl-Text-EP3-Verilog
Version:	1.00
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-EP3-Verilog - Verilog extension for the EP3 preprocessor.

%description -l pl
Text-EP3-Verilog - rozszerzenie dla preprocesora EP3.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/EP3/Verilog.pm
%{perl_sitelib}/auto/Text/EP3/Verilog
%{_mandir}/man3/*
