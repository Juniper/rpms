# $Id$

%define desktop_vendor freshrpms

Summary: Tag editor for mp3, ogg and flac files.
Name: easytag
Version: 0.30
Release: 4d.fr
License: GPL
Group: Applications/Multimedia
Source: http://dl.sf.net/easytag/%{name}-%{version}.tar.bz2
Patch10: http://dl.sf.net/easytag/patch_easytag_030_030a.diff
Patch11: http://dl.sf.net/easytag/patch_easytag_030a_030b.diff
Patch12: http://dl.sf.net/easytag/patch_easytag_030b_030c.diff
Patch13: http://dl.sf.net/easytag/patch_easytag_030c_030d.diff
URL: http://easytag.sourceforge.net/
BuildRequires: gtk+-devel >= 1.2.7, id3lib-devel >= 3.7.12
BuildRequires: libvorbis-devel >= 1.0, flac-devel, gettext, desktop-file-utils
BuildRoot: %{_tmppath}/%{name}-root

%description
EasyTAG is an utility for viewing, editing and writing tags of your
MP3, MP2, FLAC and OGG files. Its simple and nice GTK+ interface makes
tagging easier.

%prep
%setup -q
%patch10 -p1 -b .030a
%patch11 -p1 -b .030b
%patch12 -p1 -b .030c
%patch13 -p1 -b .030d

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Application                                      \
  --add-category AudioVideo                                       \
  %{buildroot}%{_datadir}/gnome/apps/Multimedia/%{name}.desktop

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc COPYING ChangeLog README TODO THANKS USERS-GUIDE
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_mandir}/man?/*

%changelog
* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 0.30-4d.fr
- Added patch for 0.30d.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.30-3c.fr
- Rebuild for Fedora Core 1.

* Thu Oct 30 2003 Matthias Saou <http://freshrpms.net/> 0.30-2c.fr
- Added patches to update to 0.30c.

* Tue Sep  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.30.

* Mon Sep  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.29.

* Tue Jul 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.28.1.

* Wed Jun  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.28.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Added patch to 0.27a.

* Fri Feb  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.27.

* Fri Jan  3 2003 Ville Skytt� <ville.skytta at iki.fi> 0.26-fr1
- Update to 0.26.

* Wed Dec 25 2002 Ville Skytt� <ville.skytta at iki.fi> 0.25b-fr1
- Update to 0.25b.
- Build with flac support.

* Thu Oct 10 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.
- Rebuild with flac support... nope, doesn't compile :-(

* Fri Sep 20 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.24.

* Fri Aug 30 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup for Red Hat Linux.
- A few %%files fixes and improvements.

* Thu Dec 18 2001 Jerome Couderc <j.couderc@ifrance.com>
- Updated for (Build)Requires entries

* Thu Sep 22 2001 Jerome Couderc <j.couderc@ifrance.com>
- Updated for /etc/X11/applnk/Multimedia/easytag.desktop

* Thu Sep 20 2001 G�tz Waschk <waschk@linux-mandrake.com> 0.15.1-1
- Updated for autoconf

* Fri Jun 2 2000 Jerome Couderc <j.couderc@ifrance.com>
- Updated to include po files into the rpm package

* Fri May 5 2000 Jerome Couderc <j.couderc@ifrance.com>
- Initial spec file.

