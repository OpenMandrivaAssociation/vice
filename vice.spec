%define	name	vice
%define version 1.20
%define rel	2
%define release %mkrel %{rel}

Summary:	VICE, the Versatile Commodore Emulator
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Emulators
Source0:	ftp://ftp.funet.fi/pub/cbm/crossplatform/emulators/VICE/%{name}-%{version}.tar.bz2
Source1:	vice-normalicons.tar.bz2
Source2:	vice-largeicons.tar.bz2
Source3:	vice-miniicons.tar.bz2
URL:		http://www.viceteam.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	readline-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libalsa-devel
BuildRequires:  libopencbm-devel
BuildRequires:	flex
BuildRequires:  automake1.7
%if %mdkversion >= 200610
BuildRequires: mkfontdir bdftopcf
BuildRequires: libxt-devel
%else
BuildRequires:  XFree86
%endif
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils


%description
VICE is a set of accurate emulators for the Commodore 64, 128, VIC20,
PET and CBM-II 8-bit computers, all of which run under the X Window
System.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -DNO_REGPARM" 
%configure2_5x --enable-gnomeui --enable-fullscreen \
%ifarch alpha
--disable-inline
%endif

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
#install menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/vice << EOF
?package(vice):command="%{_bindir}/x64" needs="X11" icon="c64icon.png" section="More Applications/Emulators" title="C64 Emulator" longtitle="Commodore 64 Emulator" 	mimetypes="application/x-d64,application/x-t64,application/x-x64" xdg="true"
?package(vice):command="%{_bindir}/x128" needs="X11" icon="c128icon.png" section="More Applications/Emulators" title="C128 Emulator" longtitle="Commodore 128 Emulator" mimetypes="application/x-d64,application/x-t64,application/x-x64" xdg="true"
?package(vice):command="%{_bindir}/xpet" needs="X11" icon="peticon.png" section="More Applications/Emulators" title="PET Emulator" longtitle="Commodore PET Emulator" mimetypes="application/x-d64,application/x-t64,application/x-x64" xdg="true"
?package(vice):command="%{_bindir}/xvic" needs="X11" icon="vic20icon.png" section="More Applications/Emulators" title="VIC 20 Emulator" longtitle="Commodore VIC 20 Emulator" mimetypes="application/x-d64,application/x-t64,application/x-x64" xdg="true"
?package(vice):command="%{_bindir}/xcbm2" needs="X11" icon="c610icon.png" section="More Applications/Emulators" title="CBM2 Emulator" longtitle="Commodore BM 2 Emulator" mimetypes="application/x-d64,application/x-t64,application/x-x64" xdg="true"
?package(vice):command="%{_bindir}/xplus4" needs="X11" icon="plus4icon.png" section="More Applications/Emulators" title="CPLUS4 Emulator" longtitle="Commodore PLUS4 Emulator" mimetypes="application/x-d64,application/x-t64,application/x-x64" xdg="true"
?package(vice):command="xvt -e %{_bindir}/c1541" needs="X11" icon="commodore.png" section="More Applications/Emulators" title="VICE disk image tool" longtitle="C1541 stand alone disk image maintenance program" xdg="true"
?package(vice):command="%{_bindir}/vsid" needs="X11" icon="commodore.png" section="Multimedia/Sound" title="VSID music player" longtitle="VICE SID music player for Commodore tunes" xdg="true"
EOF
#xdg menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-x64.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=C64 Emulator
Comment=Commodore 64 Emulator
Exec=%{_bindir}/x64 %U
Icon=c64icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-x128.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=C128 Emulator
Comment=Commodore 128 Emulator
Exec=%{_bindir}/x128 %U
Icon=c128icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-xpet.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=PET Emulator
Comment=Commodore PET Emulator
Exec=%{_bindir}/xpet %U
Icon=peticon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-xvic.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=VIC 20 Emulator
Comment=Commodore VIC 20 Emulator
Exec=%{_bindir}/xvic %U
Icon=vic20icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-xcbm2.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=CBM2 Emulator
Comment=Commodore BM 2 Emulator
Exec=%{_bindir}/xcbm2 %U
Icon=c610icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-xplus4.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=CPLUS4 Emulator
Comment=Commodore PLUS4 Emulator
Exec=%{_bindir}/xplus4 %U
Icon=plus4icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-c1541.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=VICE disk image tool
Comment=C1541 stand alone disk image maintenance program
Exec=%{_bindir}/c1541 %U
Icon=commodore
Terminal=true
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-vsid.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=VSID music player
Comment=VICE SID music player for Commodore tunes
Exec=%{_bindir}/vsid %U
Icon=commodore
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;X-MandrivaLinux-Multimedia-Sound;Audio;Player;
EOF


#install icons
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}
tar xjf %{SOURCE1} -C $RPM_BUILD_ROOT%{_iconsdir}
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
tar xjf %{SOURCE2} -C $RPM_BUILD_ROOT%{_liconsdir}
mkdir -p $RPM_BUILD_ROOT%{_miconsdir}
tar xjf %{SOURCE3} -C $RPM_BUILD_ROOT%{_miconsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info vice.info
%update_desktop_database
%{update_menus}

%postun
%_remove_install_info vice.info
%clean_desktop_database
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS FEEDBACK INSTALL README ChangeLog doc/html/plain/*
%{_bindir}/*
%{_prefix}/lib/vice
%{_mandir}/man1/*
%{_infodir}/*info*
%_datadir/applications/mandriva-*
%{_menudir}/vice
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png


