#
# Conditional build:
#
%define         orgname     kaccessible
%define         _state      stable
%define         qtver       4.8.0
#
Summary:	Accessibility services like focus tracking and a screenreader
Summary(pl.UTF-8):	kaccessible
Name:		kde4-kaccessible
Version:	4.13.0
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	43579c42720185f37f99a0cb591f3da6
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.6.3
BuildRequires:	kde4-kdelibs-devel >= %{_kdever}
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kaccessible implements a QAccessibleBridgePlugin to provide
accessibility services like focus tracking and a screenreader.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/libexec/kaccessibleapp
%dir %{_libdir}/kde4/plugins/accessiblebridge
%attr(755,root,root) %{_libdir}/kde4/plugins/accessiblebridge/kaccessiblebridge.so
%{_datadir}/dbus-1/services/org.kde.kaccessible.service
