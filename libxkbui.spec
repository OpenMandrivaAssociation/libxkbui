%define libxkbui %mklibname xkbui 1
Name: libxkbui
Summary:  The xkbui Library
Version: 1.0.2
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libxkbui-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxkbfile-devel >= 1.0.1
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xkbui Library

#-----------------------------------------------------------

%package -n %{libxkbui}
Summary:  The xkbui Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxkbui}
The xkbui Library

#-----------------------------------------------------------

%package -n %{libxkbui}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxkbui} = %{version}
Requires: libx11-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Provides: libxkbui-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxkbui}-devel
Development files for %{name}

%pre -n %{libxkbui}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxkbui}-devel
%defattr(-,root,root)
%{_libdir}/libxkbui.so
%{_libdir}/libxkbui.la
%{_libdir}/pkgconfig/xkbui.pc
%{_includedir}/X11/extensions/XKBui.h

#-----------------------------------------------------------

%package -n %{libxkbui}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxkbui}-devel = %{version}
Provides: libxkbui-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxkbui}-static-devel
Static development files for %{name}

%files -n %{libxkbui}-static-devel
%defattr(-,root,root)
%{_libdir}/libxkbui.a

#-----------------------------------------------------------

%prep
%setup -q -n libxkbui-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxkbui}
%defattr(-,root,root)
%{_libdir}/libxkbui.so.1
%{_libdir}/libxkbui.so.1.0.0


