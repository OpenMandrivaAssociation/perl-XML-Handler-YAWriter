%define upstream_name    XML-Handler-YAWriter
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	XML::Handler::YAWriter perl module
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-libxml-perl >= 0.06
BuildArch:	noarch

Provides:	XML-Handler-YAWriter = %{version}-%{release}

%description
YAWriter implements Yet Another XML::Handler::Writer. The reasons for
this one are that I needed a flexible escaping technique, and want
some kind of pretty printing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%__rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc README
%{_bindir}/*
%{perl_vendorlib}/XML/Handler/*
%{_mandir}/man[13]/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.230.0-4mdv2012.0
+ Revision: 765844
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.230.0-2
+ Revision: 667427
- mass rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 408239
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.23-12mdv2009.0
+ Revision: 224627
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.23-11mdv2008.1
+ Revision: 180657
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 0.23-10mdv2008.0
+ Revision: 64205
- rebuild


* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:43:51 (54168)
- rebuild

* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:35:45 (54167)
Import perl-XML-Handler-YAWriter

* Sun Apr 30 2006 Olivier Thauvin <nanardon@mandriva.org> 0.23-8mdk
- rebuild && %%mkrel

* Sat Jan 01 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.23-7mdk
- "Birthday rebuild" and q/Happy new year/;

