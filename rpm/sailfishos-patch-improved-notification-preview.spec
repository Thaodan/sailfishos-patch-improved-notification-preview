# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-patch-improved-notification-preview

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Moves enlargened app icon inside the preview bubble. Provides settings to customize notification preview's look and behavior.
Version:    0.4.3
Release:    2
Group:      Applications/Productivity
License:    GPLv2+
BuildArch:  noarch
URL:        https://github.com/Ingvix/sailfishos-patch-improved-notification-preview
Source0:    %{name}-%{version}.tar.bz2
Source100:  sailfishos-patch-improved-notification-preview.yaml
Requires:   patchmanager
Requires:   lipstick-jolla-home-qt5 >= 0.36.30-10.3.1.jolla
Requires:   sailfish-version >= 2.0.2-10.35.43.jolla
BuildRequires:  pkgconfig(Qt5Core)

%description
Patch that makes notification portrait-screen-wide and moves enlargened icon inside the notification bubble. Swipe notification left to dismiss it and right to remove it.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
/usr/sbin/patchmanager -u sailfishos-patch-notification-dismiss-remove || true
# << install pre
%qmake5_install

# >> install post
# << install post

%preun
# >> preun
if [ -x /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-patch-improved-notification-preview || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager
%{_datadir}/translations
# >> files
# << files
