%define name	gtk-iptables
%define version	0.5.1
%define release  4

Name: 	 	%{name}
Summary: 	GTK-based frontend for iptables
Version: 	%{version}
Release: 	%{release}

Source0:		%{name}-%{version}.tar.bz2
source1:		.abf.yml
patch0:			gtk-iptables-0.5.1.printf.patch
URL:		http://gtk-iptables.sourceforge.net
License:	GPL
Group:		System/Configuration/Networking
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	gksu userspace-ipfilter
Obsoletes:	gtkiptables
Provides:	gtkiptables

%description
Gtk-IPTables is a GTK-based frontend for iptables written in C. You can
create rules for all chains for Filter, NAT, and Mangle tables.

%prep
%setup -q
%patch0 -p1 -b .printf

%build
%configure2_5x
%make

%install
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=gksu gtkiptables
Icon=networking_configuration_section
Name=GTK-IPTables
Comment=IPTables Rules Configuration
Categories=Network;
EOF

%find_lang %name || touch %{name}.lang

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/gtkiptables
%{_datadir}/applications/mandriva-%name.desktop
%{_datadir}/pixmaps/*


%changelog
* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5.1-3mdv2009.0
+ Revision: 246693
- rebuild
- fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 27 2007 Jérôme Soyer <saispo@mandriva.org> 0.5.1-1mdv2008.1
+ Revision: 138403
- Fix BuildRequires
- New release

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.4.21-3mdv2008.1
+ Revision: 131725
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import gtk-iptables


* Tue Nov 02 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.4.21-3mdk
- rebuild with current autotools

* Wed Dec 17 2003 Marcel Pol <mpol@mandrake.org> 0.4.21-2mdk
- depend on userspace-ipfilter
- 64bit buildrequires

* Wed Apr 2 2003 Austin Acton <aacton@yorku.ca> 0.4.21-1mdk
- 0.4.21

* Sun Mar 23 2003 Austin Acton <aacton@yorku.ca> 0.4.1-1mdk
- initial package
