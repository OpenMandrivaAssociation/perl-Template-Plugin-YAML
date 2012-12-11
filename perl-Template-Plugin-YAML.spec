%define upstream_name	 Template-Plugin-YAML
%define upstream_version 1.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Plugin interface to YAML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(YAML)
BuildRequires:	perl(Template)
BuildArch:	noarch

%description
This is a simple Template Toolkit Plugin Interface to the YAML module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test 

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Template
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-1mdv2010.0
+ Revision: 405536
- rebuild using %%perl_convert_version

* Wed Dec 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2009.1
+ Revision: 315132
- new version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.22-4mdv2009.0
+ Revision: 258485
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.22-3mdv2009.0
+ Revision: 246511
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.22-1mdv2008.1
+ Revision: 123634
- kill re-definition of %%buildroot on Pixel's request


(none)