%define module	Template-Plugin-YAML
%define name	perl-%{module}
%define version 1.22
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Plugin interface to YAML
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		%{module}-%{version}.tar.bz2
Patch0:		perl-Template-Plugin-YAML-version-remove.patch
BuildArch:	noarch
BuildRequires:	perl-YAML
BuildRequires:	perl-Template
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a simple Template Toolkit Plugin Interface to the YAML module.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .noyamlversion

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test 

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Template
%{_mandir}/*/*



