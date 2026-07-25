%define modname	XML-Handler-YAWriter
%define modver	0.23

Summary:	XML::Handler::YAWriter perl module
Name:		perl-%{modname}
Version:	%{modver}
Release:	20
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-Handler-YAWriter
Source0:	https://cpan.metacpan.org/authors/id/K/KR/KRAEHE/XML-Handler-YAWriter-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-libxml-perl >= 0.06
Provides:	XML-Handler-YAWriter = %{version}-%{release}

%description
YAWriter implements Yet Another XML::Handler::Writer. The reasons for
this one are that I needed a flexible escaping technique, and want
some kind of pretty printing.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc README
%{_bindir}/*
%{perl_vendorlib}/XML/Handler/*
%{_mandir}/man1/*
%{_mandir}/man3/*

