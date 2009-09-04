%define name	gtk-iptables
%define version	0.5.1
%define release  %mkrel 4

Name: 	 	%{name}
Summary: 	GTK-based frontend for iptables
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://gtk-iptables.sourceforge.net
License:	GPL
Group:		System/Configuration/Networking
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk2-devel
Requires:	gksu userspace-ipfilter
Obsoletes:	gtkiptables
Provides:	gtkiptables

%description
Gtk-IPTables is a GTK-based frontend for iptables written in C. You can
create rules for all chains for Filter, NAT, and Mangle tables.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
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

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/gtkiptables
%{_datadir}/applications/mandriva-%name.desktop
%{_datadir}/pixmaps/*
