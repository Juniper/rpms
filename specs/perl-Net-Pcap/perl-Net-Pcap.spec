# $Id$
# Authority: dries
# Upstream: Marco Carnut <kiko$tempest,com,br>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Pcap

Summary: Interface to pcap(3) LBL packet capture library
Name: perl-Net-Pcap
Version: 0.05
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Pcap/

Source: http://search.cpan.org/CPAN/authors/id/K/KC/KCARNUT/Net-Pcap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, libpcap

%description
This module is an interface to pcap(3) LBL packet capture library.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/Pcap.pm
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/Pcap/

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
