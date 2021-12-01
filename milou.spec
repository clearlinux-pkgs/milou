#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : milou
Version  : 5.23.4
Release  : 58
URL      : https://download.kde.org/stable/plasma/5.23.4/milou-5.23.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.23.4/milou-5.23.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: milou-data = %{version}-%{release}
Requires: milou-lib = %{version}-%{release}
Requires: milou-license = %{version}-%{release}
Requires: milou-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
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
%setup -q -n milou-5.23.4
cd %{_builddir}/milou-5.23.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638356638
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1638356638
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/milou
cp %{_builddir}/milou-5.23.4/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/milou/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/milou-5.23.4/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/milou/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/milou-5.23.4/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/milou/2123756e0b1fc8243547235a33c0fcabfe3b9a51
cp %{_builddir}/milou-5.23.4/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/milou/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
cp %{_builddir}/milou-5.23.4/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/milou/19d98e1b6f8ef12849ea4012a052d3907f336c91
cp %{_builddir}/milou-5.23.4/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/milou/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/milou-5.23.4/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/milou/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/milou-5.23.4/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/milou/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/milou-5.23.4/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/milou/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang milou
%find_lang plasma_applet_org.kde.milou

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/metainfo/org.kde.milou.appdata.xml
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/SearchField.qml
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/globals.js
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/previews/TextPreview.qml
/usr/share/plasma/plasmoids/org.kde.milou/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.milou/metadata.json

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmilou.so.5
/usr/lib64/libmilou.so.5.23.4
/usr/lib64/qt5/qml/org/kde/milou/ResultDelegate.qml
/usr/lib64/qt5/qml/org/kde/milou/ResultsListView.qml
/usr/lib64/qt5/qml/org/kde/milou/ResultsListViewDelegate.qml
/usr/lib64/qt5/qml/org/kde/milou/ResultsView.qml
/usr/lib64/qt5/qml/org/kde/milou/globals.js
/usr/lib64/qt5/qml/org/kde/milou/libmilouqmlplugin.so
/usr/lib64/qt5/qml/org/kde/milou/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/milou/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/milou/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/milou/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/milou/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/milou/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/milou/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f milou.lang -f plasma_applet_org.kde.milou.lang
%defattr(-,root,root,-)

