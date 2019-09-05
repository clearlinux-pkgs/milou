#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : milou
Version  : 5.16.5
Release  : 25
URL      : https://download.kde.org/stable/plasma/5.16.5/milou-5.16.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.16.5/milou-5.16.5.tar.xz
Source1 : https://download.kde.org/stable/plasma/5.16.5/milou-5.16.5.tar.xz.sig
Summary  : A dedicated search application built on top of Baloo
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: milou-data = %{version}-%{release}
Requires: milou-lib = %{version}-%{release}
Requires: milou-license = %{version}-%{release}
Requires: milou-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : krunner-dev
BuildRequires : plasma-framework-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the milou package.
Group: Data

%description data
data components for the milou package.


%package lib
Summary: lib components for the milou package.
Group: Libraries
Requires: milou-data = %{version}-%{release}
Requires: milou-license = %{version}-%{release}

%description lib
lib components for the milou package.


%package license
Summary: license components for the milou package.
Group: Default

%description license
license components for the milou package.


%package locales
Summary: locales components for the milou package.
Group: Default

%description locales
locales components for the milou package.


%prep
%setup -q -n milou-5.16.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567647620
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567647620
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/milou
cp COPYING %{buildroot}/usr/share/package-licenses/milou/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/milou/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang milou
%find_lang plasma_applet_org.kde.milou

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/miloutextpreview.desktop
/usr/share/kservices5/plasma-applet-org.kde.milou.desktop
/usr/share/kservicetypes5/miloupreviewplugin.desktop
/usr/share/metainfo/org.kde.milou.appdata.xml
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/SearchField.qml
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/globals.js
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/previews/Audio.qml
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/previews/TextPreview.qml
/usr/share/plasma/plasmoids/org.kde.milou/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.milou/metadata.json

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmilou.so.5
/usr/lib64/libmilou.so.5.16.5
/usr/lib64/qt5/plugins/miloutextplugin.so
/usr/lib64/qt5/qml/org/kde/milou/ResultDelegate.qml
/usr/lib64/qt5/qml/org/kde/milou/ResultsListView.qml
/usr/lib64/qt5/qml/org/kde/milou/ResultsListViewDelegate.qml
/usr/lib64/qt5/qml/org/kde/milou/ResultsView.qml
/usr/lib64/qt5/qml/org/kde/milou/globals.js
/usr/lib64/qt5/qml/org/kde/milou/libmilouqmlplugin.so
/usr/lib64/qt5/qml/org/kde/milou/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/milou/COPYING
/usr/share/package-licenses/milou/COPYING.LIB

%files locales -f milou.lang -f plasma_applet_org.kde.milou.lang
%defattr(-,root,root,-)

