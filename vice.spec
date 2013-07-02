%define Werror_cflags %nil

Summary:	The Versatile Commodore Emulator
Name:		vice
Version:	2.4
Release:	2
License:	GPLv2
Group:		Emulators
URL:		http://www.viceteam.org/
Source0:	http://sourceforge.net/projects/vice-emu/files/development-releases/%{name}-%{version}.tar.gz
Source1:	vice-normalicons.tar.bz2
Source2:	vice-largeicons.tar.bz2
Source3:	vice-miniicons.tar.bz2
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	ffmpeg0.7-devel
BuildRequires:	readline-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gdkglext-1.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	flex
BuildRequires:	mkfontdir
BuildRequires:	bdftopcf
Requires:	vice-binaries = %{version}-%{release}

%description
VICE is a set of accurate emulators for the Commodore 64, 128, VIC20,
PET and CBM-II 8-bit computers, all of which run under the X Window
System.

%package sdl
Summary:	SDL set of vice emulators binaries
Group:		Emulators
Requires:	%{name} = %{version}-%{release}
Provides:	vice-binaries = %{version}-%{release}

%description sdl
SDL set of vice emulators binaries.

%package gtk
Summary:	GTK set of vice emulators binaries
Group:		Emulators
Requires:	%{name} = %{version}-%{release}
Provides:	vice-binaries = %{version}-%{release}

%description gtk
GTK set of vice emulators binaries.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -DNO_REGPARM"
%configure2_5x --enable-sdlui --enable-fullscreen
%make

make install DESTDIR=`pwd`/sdl

pushd sdl/usr/bin
for i in *
do
	mv $i $i-sdl
done
popd

make clean

%configure2_5x --enable-gnomeui --enable-fullscreen
%make

%install
%makeinstall_std

cp sdl/%{_bindir}/*-sdl %{buildroot}%{_bindir}/

#xdg menus
#============GTK============
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-x64-gtk.desktop << EOF
[Desktop Entry]
Name=C64 Emulator (GTK)
Comment=Commodore 64 Emulator
Exec=%{_bindir}/x64 %U
Icon=c64icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-x128-gtk.desktop << EOF
[Desktop Entry]
Name=C128 Emulator (GTK)
Comment=Commodore 128 Emulator
Exec=%{_bindir}/x128 %U
Icon=c128icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xpet-gtk.desktop << EOF
[Desktop Entry]
Name=PET Emulator (GTK)
Comment=Commodore PET Emulator
Exec=%{_bindir}/xpet %U
Icon=peticon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xvic-gtk.desktop << EOF
[Desktop Entry]
Name=VIC 20 Emulator (GTK)
Comment=Commodore VIC 20 Emulator
Exec=%{_bindir}/xvic %U
Icon=vic20icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xcbm2-gtk.desktop << EOF
[Desktop Entry]
Name=CBM2 Emulator (GTK)
Comment=Commodore BM 2 Emulator
Exec=%{_bindir}/xcbm2 %U
Icon=c610icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xplus4-gtk.desktop << EOF
[Desktop Entry]
Name=CPLUS4 Emulator (GTK)
Comment=Commodore PLUS4 Emulator
Exec=%{_bindir}/xplus4 %U
Icon=plus4icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-c1541-gtk.desktop << EOF
[Desktop Entry]
Name=VICE disk image tool (GTK)
Comment=C1541 stand alone disk image maintenance program
Exec=%{_bindir}/c1541 %U
Icon=commodore
Terminal=true
Type=Application
StartupNotify=true
Categories=Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-vsid-gtk.desktop << EOF
[Desktop Entry]
Name=VSID music player (GTK)
Comment=VICE SID music player for Commodore tunes
Exec=%{_bindir}/vsid %U
Icon=commodore
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;Player;
EOF
#============GTK============

#============SDL============
%__cat > %{buildroot}%{_datadir}/applications/mandriva-x64-sdl.desktop << EOF
[Desktop Entry]
Name=C64 Emulator (SDL)
Comment=Commodore 64 Emulator
Exec=%{_bindir}/x64-sdl %U
Icon=c64icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Game;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-x128-sdl.desktop << EOF
[Desktop Entry]
Name=C128 Emulator (SDL)
Comment=Commodore 128 Emulator
Exec=%{_bindir}/x128-sdl %U
Icon=c128icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xpet-sdl.desktop << EOF
[Desktop Entry]
Name=PET Emulator (SDL)
Comment=Commodore PET Emulator
Exec=%{_bindir}/xpet-sdl %U
Icon=peticon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xvic-sdl.desktop << EOF
[Desktop Entry]
Name=VIC 20 Emulator (SDL)
Comment=Commodore VIC 20 Emulator
Exec=%{_bindir}/xvic-sdl %U
Icon=vic20icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xcbm2-sdl.desktop << EOF
[Desktop Entry]
Name=CBM2 Emulator (SDL)
Comment=Commodore BM 2 Emulator
Exec=%{_bindir}/xcbm2-sdl %U
Icon=c610icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xplus4-sdl.desktop << EOF
[Desktop Entry]
Name=CPLUS4 Emulator (SDL)
Comment=Commodore PLUS4 Emulator
Exec=%{_bindir}/xplus4-sdl %U
Icon=plus4icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-c1541-sdl.desktop << EOF
[Desktop Entry]
Name=VICE disk image tool (SDL)
Comment=C1541 stand alone disk image maintenance program
Exec=%{_bindir}/c1541-sdl %U
Icon=commodore
Terminal=true
Type=Application
StartupNotify=true
Categories=Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-vsid-sdl.desktop << EOF
[Desktop Entry]
Name=VSID music player (SDL)
Comment=VICE SID music player for Commodore tunes
Exec=%{_bindir}/vsid-sdl %U
Icon=commodore
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;Player;
EOF
#============SDL============

#install icons
%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
tar xjf %{SOURCE1} -C %{buildroot}%{_iconsdir}/hicolor/32x32/apps
tar xjf %{SOURCE2} -C %{buildroot}%{_iconsdir}/hicolor/48x48/apps
tar xjf %{SOURCE3} -C %{buildroot}%{_iconsdir}/hicolor/16x16/apps

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS FEEDBACK INSTALL README ChangeLog doc/html/plain/*
%{_libdir}/vice
%{_mandir}/man1/*
%{_infodir}/%{name}*
%{_iconsdir}/hicolor/*/apps/*.png

%files sdl
%{_bindir}/*-sdl
%{_datadir}/applications/*-sdl.desktop

%files gtk
%{_bindir}/*
%exclude %{_bindir}/*-sdl
%{_datadir}/applications/*-gtk.desktop

