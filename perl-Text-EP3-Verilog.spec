%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Text-EP3-Verilog perl module
Summary(pl):	Modu³ perla Text-EP3-Verilog
Name:		perl-Text-EP3-Verilog
Version:	1.00
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-EP3-Verilog-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text-EP3-Verilog - Verilog extension for the EP3 preprocessor.

%description -l pl
Text-EP3-Verilog - rozszerzenie dla preprocesora EP3.

%prep
%setup -q -n Text-EP3-Verilog-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/EP3/Verilog
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Text/EP3/Verilog.pm
%{perl_sitelib}/auto/Text/EP3/Verilog
%{perl_sitearch}/auto/Text/EP3/Verilog

%{_mandir}/man3/*
