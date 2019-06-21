%define Werror_cflags %nil
%define _disable_rebuild_configure 1

Summary:	VICE, the Versatile Commodore Emulator
Name:		vice
Version:	3.3
Release:	1
License:	GPLv2+
Group:		Emulators
Url:		http://vice-emu.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/vice-emu/releases/vice-%{version}.tar.gz
Source1:	vice-normalicons.tar.bz2
Source2:	vice-largeicons.tar.bz2
Source3:	vice-miniicons.tar.bz2
BuildRequires:	bdftopcf
BuildRequires:	flex
BuildRequires:	mkfontdir
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	readline-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gdkglext-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	xa
Requires:	vice-binaries = %{EVRD}

%description
VICE is a set of accurate emulators for the Commodore 64, 128, VIC20,
PET and CBM-II 8-bit computers, all of which run under the X Window
System.

%files
%doc AUTHORS FEEDBACK INSTALL README ChangeLog
%{_libdir}/vice
%{_mandir}/man1/*
%{_infodir}/%{name}*
%{_iconsdir}/hicolor/*/apps/*.png

#----------------------------------------------------------------------------

%package sdl
Summary:	SDL set of vice emulators binaries
Group:		Emulators
Requires:	%{name} = %{EVRD}
Provides:	vice-binaries = %{EVRD}

%description sdl
SDL set of vice emulators binaries.

%files sdl
%{_bindir}/*-sdl
%{_datadir}/applications/*-sdl.desktop

#----------------------------------------------------------------------------

%package gtk
Summary:	GTK set of vice emulators binaries
Group:		Emulators
Requires:	%{name} = %{EVRD}
Provides:	vice-binaries = %{EVRD}

%description gtk
GTK set of vice emulators binaries.

%files gtk
%{_bindir}/*
%exclude %{_bindir}/*-sdl
%{_datadir}/applications/*-gtk.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
# --disable-option-checking is needed because the configure
# macro adds --disable-static, --disable-rpath and a few other
# generic autoconf-isms
%define common_args \\\
	--enable-fullscreen \\\
	--enable-external-ffmpeg \\\
	--enable-ethernet \\\
	--disable-arch \\\
	--with-ui-threads \\\
	--with-sdlsound \\\
	--disable-option-checking


%configure \
	--enable-sdlui2 \
	%{common_args}
%make

make install DESTDIR=`pwd`/sdl

pushd sdl/usr/bin
for i in *
do
	mv $i $i-sdl
done
popd

make clean

%configure \
	--enable-native-gtk3ui \
	%{common_args}
%make

%install
%makeinstall_std

cp sdl%{_bindir}/*-sdl %{buildroot}%{_bindir}/
cp -af sdl%{_libdir}/vice %{buildroot}%{_libdir}/

#xdg menus
#============GTK============
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-x64-gtk.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-x128-gtk.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-xpet-gtk.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-xvic-gtk.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-xcbm2-gtk.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-xplus4-gtk.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-c1541-gtk.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-vsid-gtk.desktop << EOF
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
cat > %{buildroot}%{_datadir}/applications/mandriva-x64-sdl.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-x128-sdl.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-xpet-sdl.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-xvic-sdl.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-xcbm2-sdl.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-xplus4-sdl.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-c1541-sdl.desktop << EOF
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

cat > %{buildroot}%{_datadir}/applications/mandriva-vsid-sdl.desktop << EOF
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
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
tar xjf %{SOURCE1} -C %{buildroot}%{_iconsdir}/hicolor/32x32/apps
tar xjf %{SOURCE2} -C %{buildroot}%{_iconsdir}/hicolor/48x48/apps
tar xjf %{SOURCE3} -C %{buildroot}%{_iconsdir}/hicolor/16x16/apps
