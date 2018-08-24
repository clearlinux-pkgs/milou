#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : milou
Version  : 5.13.4
Release  : 1
URL      : https://download.kde.org/stable/plasma/5.13.4/milou-5.13.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.13.4/milou-5.13.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: milou-lib
Requires: milou-license
Requires: milou-data
Requires: milou-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kdeclarative-dev
BuildRequires : kpackage-dev
BuildRequires : krunner-dev
BuildRequires : kwindowsystem-dev
BuildRequires : plasma-framework-dev
BuildRequires : qtbase-dev qtbase-extras mesa-dev

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
Requires: milou-data
Requires: milou-license

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
%setup -q -n milou-5.13.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535149685
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535149685
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/milou
cp COPYING %{buildroot}/usr/share/doc/milou/COPYING
cp COPYING.LIB %{buildroot}/usr/share/doc/milou/COPYING.LIB
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
/usr/lib64/libmilou.so.5.13.4
/usr/lib64/qt5/plugins/miloutextplugin.so
/usr/lib64/qt5/qml/org/kde/milou/ResultDelegate.qml
/usr/lib64/qt5/qml/org/kde/milou/ResultsListView.qml
/usr/lib64/qt5/qml/org/kde/milou/ResultsListViewDelegate.qml
/usr/lib64/qt5/qml/org/kde/milou/ResultsView.qml
/usr/lib64/qt5/qml/org/kde/milou/globals.js
/usr/lib64/qt5/qml/org/kde/milou/libmilouqmlplugin.so
/usr/lib64/qt5/qml/org/kde/milou/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/milou/COPYING
/usr/share/doc/milou/COPYING.LIB

%files locales -f milou.lang -f plasma_applet_org.kde.milou.lang
%defattr(-,root,root,-)

