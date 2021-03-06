# $Id$
# Authority: shuff
# Upstream: W3C QA-dev Team <public-qa-dev$w3,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name W3C-LinkChecker

Summary: Check the validity of links in an HTML or XHTML document
Name: perl-%{real_name}
Version: 4.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/W3C-LinkChecker/

Source: http://search.cpan.org/CPAN/authors/id/S/SC/SCOP/W3C-LinkChecker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(CGI)
BuildRequires: perl(CGI::Carp)
BuildRequires: perl(CGI::Cookie)
BuildRequires: perl(CSS::DOM) >= 0.09
BuildRequires: perl(CSS::DOM::Constants)
BuildRequires: perl(CSS::DOM::Style)
BuildRequires: perl(CSS::DOM::Util)
BuildRequires: perl(Config::General) >= 2.06
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long) >= 2.17
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTML::Parser) >= 3.2
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response) >= 1.5
BuildRequires: perl(LWP::RobotUA) >= 1.19
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Locale::Country)
BuildRequires: perl(Locale::Language)
BuildRequires: perl(Net::IP)
BuildRequires: perl(Net::hostent)
BuildRequires: perl(Socket)
BuildRequires: perl(Term::ReadKey) >= 2
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Wrap)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(URI) >= 1.31
BuildRequires: perl(URI::Escape)
BuildRequires: perl(URI::file)
BuildRequires: perl(perl5lib)
Requires: perl(CGI)
Requires: perl(CGI::Carp)
Requires: perl(CGI::Cookie)
Requires: perl(CSS::DOM) >= 0.09
Requires: perl(CSS::DOM::Constants)
Requires: perl(CSS::DOM::Style)
Requires: perl(CSS::DOM::Util)
Requires: perl(Config::General) >= 2.06
Requires: perl(File::Spec)
Requires: perl(Getopt::Long) >= 2.17
Requires: perl(HTML::Entities)
Requires: perl(HTML::Parser) >= 3.2
Requires: perl(HTTP::Request)
Requires: perl(HTTP::Response) >= 1.5
Requires: perl(LWP::RobotUA) >= 1.19
Requires: perl(LWP::UserAgent)
Requires: perl(Locale::Country)
Requires: perl(Locale::Language)
Requires: perl(Net::IP)
Requires: perl(Net::hostent)
Requires: perl(Socket)
Requires: perl(Term::ReadKey) >= 2
Requires: perl(Text::Wrap)
Requires: perl(Time::HiRes)
Requires: perl(URI) >= 1.31
Requires: perl(URI::Escape)
Requires: perl(URI::file)
Requires: perl(perl5lib)

Provides: %{_bindir}/checklink
Provides: config(checklink)

%filter_from_requires /^perl*/d
%filter_setup

%description
checklink is a program that reads an HTML or XHTML document, extracts a list of
anchors and lists and checks that no anchor is defined twice and that all the
links are dereferenceable, including the fragments. It warns about HTTP
redirects, including directory redirects, and can check recursively a part of a
web site.

The program can be used either as a command line tool or as a CGI script.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/w3c
%{__install} -m0644 etc/checklink.conf %{buildroot}%{_sysconfdir}/w3c

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog ChangeLog.old MANIFEST NEWS README SIGNATURE
%doc docs/ images/
%doc etc/checklink.conf
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/W3C/
%{perl_vendorlib}/W3C/*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/w3c/checklink.conf

%changelog
* Wed May 05 2010 Steve Huff <shuff@vecna.org>
- Added some uncaptured dependencies.

* Tue May  4 2010 Christoph Maser <cmr@financial.com> - 4.6-1
- Updated to version 4.6.

* Mon Feb 22 2010 Steve Huff <shuff@vecna.org> - 4.5-1
- Initial package.
