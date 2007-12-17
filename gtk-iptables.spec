%define name	gtk-iptables
%define version	0.4.21
%define release  %mkrel 3

Name: 	 	%{name}
Summary: 	GTK-based frontend for iptables
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://gtk-iptables.sourceforge.net
License:	GPL
Group:		System/Configuration/Networking
BuildRequires:	gtk-devel automake1.8
Requires:	gksu userspace-ipfilter
Obsoletes:	gtkiptables
Provides:	gtkiptables

%description
Gtk-IPTables is a GTK-based frontend for iptables written in C. You can
create rules for all chains for Filter, NAT, and Mangle tables.

%prep
%setup -q

%build
export FORCE_AUTOCONF_2_5=1
aclocal-1.8
automake-1.8 -a -c --foreign
autoconf
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="gksu gtkiptables" icon="networking_configuration_section.png" needs="x11" title="GTK-IPTables" longtitle="IPTables Rules Configuration" section="Configuration/Networking"
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING NEWS
%{_bindir}/gtkiptables
%{_menudir}/%name

