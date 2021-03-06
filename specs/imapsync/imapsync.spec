# $Id$3.19
# Authority: dag

Summary: Tool to migrate across IMAP servers
Name: imapsync
Version: 1.452
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.linux-france.org/prj/imapsync/

Source: http://www.linux-france.org/prj/imapsync/dist/imapsync-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Mail::IMAPClient) >= 3.19
Requires: perl(Date::Manip)
Requires: perl(Digest::MD5)
Requires: perl(IO::Socket::SSL)
Requires: perl(Mail::IMAPClient) >= 3.19
Requires: perl(Term::ReadKey)
Requires: perl(Digest::HMAC_MD5)
#Requires: perl(Digest::MD5::M4p)
#Requires: perl(Net::SSLeay)

%filter_from_requires /^perl(--prefix2)/d
%filter_setup

%description
imapsync is a tool for facilitating incremental recursive IMAP
transfers from one mailbox to another. It is useful for mailbox
migration, and reduces the amount of data transferred by only copying
messages that are not present on both servers. Read, unread, and
deleted flags are preserved, and the process can be stopped and
resumed. The original messages can optionally be deleted after a
successful transfer.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING CREDITS FAQ INSTALL README TODO
%doc %{_mandir}/man1/imapsync.1*
%{_bindir}/imapsync

%clean
%{__rm} -rf %{buildroot}

%changelog
* Mon Aug 01 2011 Dag Wieers <dag@wieers.com> - 1.452-1
- Updated to release 1.452.

* Tue Sep 07 2010 Dag Wieers <dag@wieers.com> - 1.350-1
- Updated to release 1.350.

* Wed Jan 13 2010 Steve Huff <shuff@vecna.org> - 1.293-1
- Updated to version 1.293.

* Sun Dec 20 2009 Steve Huff <shuff@vecna.org> - 1.286-2
- Added missing Perl dependencies (reported by John Thomas).

* Thu Sep 10 2009 Dag Wieers <dag@wieers.com> - 1.286-1
- Updated to release 1.286.

* Thu Jul 09 2009 Christoph Maser <cmr@financial.com> - 1.285-1
- Updated to release 1.285.

* Mon Jun 30 2008 Dag Wieers <dag@wieers.com> - 1.255-1
- Updated to release 1.255.

* Fri May 09 2008 Dag Wieers <dag@wieers.com> - 1.252-1
- Updated to release 1.252.

* Sun Apr 27 2008 Dag Wieers <dag@wieers.com> - 1.250-1
- Updated to release 1.250.

* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 1.249-1
- Updated to release 1.249.

* Mon Feb 11 2008 Dag Wieers <dag@wieers.com> - 1.241-1
- Updated to release 1.241.

* Thu Nov 22 2007 Dag Wieers <dag@wieers.com> - 1.233-1
- Updated to release 1.233.

* Thu Sep 13 2007 Dag Wieers <dag@wieers.com> - 1.223-1
- Updated to release 1.223.

* Thu Aug 16 2007 Fabian Arrotin <fabian.arrotin@arrfab.net> - 1.219-1
- Update to 1.219.
- Cosmetic changes for Requires: specific to RHEL/CentOS.

* Mon Mar 19 2007 Neil Brown <neilb@inf.ed.ac.uk>
- Packaged up source tarball into the RPM. Had to add a fix
  to stop the perl_requires script wrongly matching on "use --prefix"
  in the docs as a genuine perl "use module;"
