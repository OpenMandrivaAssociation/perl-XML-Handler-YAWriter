%define	pdir	XML
%define	pnam	Handler-YAWriter
%define name    perl-%{pdir}-%{pnam}
%define version 0.23
%define release %mkrel 10

Summary:	XML::Handler::YAWriter perl module
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-libxml-perl >= 0.06
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Url: http://www.cpan.org/
Obsoletes:	%{pdir}-%{pnam}
Provides:	%{pdir}-%{pnam}

%description
YAWriter implements Yet Another XML::Handler::Writer. The reasons for
this one are that I needed a flexible escaping technique, and want
some kind of pretty printing.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT

%makeinstall DESTDIR=$RPM_BUILD_ROOT

%{__rm} -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{perl_vendorlib}/XML/Handler/*
%{_mandir}/man[13]/*


